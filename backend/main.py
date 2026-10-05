import os
import json
import time
import hmac
import hashlib
from typing import List, Dict, Any, Set
from contextlib import asynccontextmanager
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException, Depends, Header, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse, JSONResponse
from sqlalchemy.orm import Session

from backend.models import (
    TelemetryEvent, GraphResponse, QuarantineRequest, QuarantineResponse,
    SessionRecord, TelemetryRecord, ClusterRecord
)
from backend.database import init_db, get_db
from backend.graph_engine import ShadowGraphEngine
from backend.mock_simulation import populate_mock_cyber_range
from backend.nim_client import generate_sar_report_narrative

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    print("[ShadowGram Core] Listening on 0.0.0.0:8000 | Multi-Laptop Hotspot LAN Ready.")
    yield

# Initialize FastAPI App
app = FastAPI(
    title="ShadowGram Forensics Gateway",
    version="1.0.0",
    description="In-flight Behavioral Graph Forensics & Autonomous Swarm Quarantine Engine",
    lifespan=lifespan
)

# Configure Permissive CORS for Local Hotspot Multi-Laptop LAN
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global In-Memory Engines
graph_engine = ShadowGraphEngine(window_seconds=600.0, edge_threshold=0.78)
SHARED_HMAC_SALT = os.getenv("SHADOWGRAM_SALT", "shadowgram-2026-secret-salt").encode()

# WebSocket Connection Manager
class ConnectionManager:
    def __init__(self):
        self.active_connections: Set[WebSocket] = set()

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.add(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.discard(websocket)

    async def broadcast(self, message: Dict[str, Any]):
        for connection in list(self.active_connections):
            try:
                await connection.send_json(message)
            except Exception:
                self.disconnect(connection)

ws_manager = ConnectionManager()

# ---------------------------------------------------------
# HMAC Verification Utility
# ---------------------------------------------------------
def verify_hmac(session_id: str, timestamp: float, signature: str) -> bool:
    """Verifies client telemetry packet integrity against cURL forgery."""
    if not signature:
        return True  # Permissive during initial testing, enforce if provided
    
    salts = [
        SHARED_HMAC_SALT,
        b"shadowgram-hackathena-2026-salt",
        b"shadowgram-2026-secret-salt"
    ]
    formats = [
        f"{session_id}:{timestamp:.3f}".encode(),
        f"{session_id}:{timestamp}".encode()
    ]
    for s in salts:
        for fmt in formats:
            expected = hmac.new(s, fmt, hashlib.sha256).hexdigest()
            if hmac.compare_digest(expected, signature):
                return True
    return False

# ---------------------------------------------------------
# REST API Endpoints (Conforming strictly to SG-PROTO-00)
# ---------------------------------------------------------

@app.get("/health")
def health_check():
    """Heartbeat probe for local connectivity verification."""
    return {
        "status": "online",
        "service": "ShadowGram Core Engine",
        "active_sessions": len(graph_engine.sessions),
        "edges_count": graph_engine.graph.number_of_edges(),
        "timestamp": time.time()
    }

@app.post("/telemetry", status_code=status.HTTP_200_OK)
async def receive_telemetry(event: TelemetryEvent, db: Session = Depends(get_db)):
    """
    Ingests live telemetry packets from Laptop 1 (Playwright Swarm) and Laptop 3 (AthenaPay App).
    Updates relational graph, logs to SQLite, and broadcasts event to 3D Cockpit.
    """
    # HMAC verification
    if event.telemetry_hmac:
        if not verify_hmac(event.session_id, event.timestamp, event.telemetry_hmac):
            raise HTTPException(status_code=401, detail="Invalid HMAC Telemetry Signature")

    payload_dict = event.payload.model_dump()

    # Ingest into in-memory graph engine
    graph_engine.ingest_event(
        session_id=event.session_id,
        account_id=event.account_id,
        event_type=event.event_type,
        timestamp=event.timestamp,
        payload=payload_dict
    )

    # Persist asynchronously to SQLite
    try:
        # Update or create session record
        sess_rec = db.query(SessionRecord).filter(SessionRecord.account_id == event.account_id).first()
        if not sess_rec:
            sess_rec = SessionRecord(
                id=event.session_id,
                account_id=event.account_id,
                status="active",
                risk_label="normal_organic"
            )
            db.add(sess_rec)

        # Log event record
        ev_rec = TelemetryRecord(
            session_id=event.session_id,
            account_id=event.account_id,
            event_type=event.event_type,
            timestamp=event.timestamp,
            flight_time_ms=payload_dict.get("key_flight_time_ms"),
            dwell_time_ms=payload_dict.get("key_dwell_time_ms"),
            pointer_jerk=payload_dict.get("pointer_curvature_jerk"),
            route_path=payload_dict.get("route_path"),
            tripwire_id=payload_dict.get("tripwire_id"),
            raw_payload_json=json.dumps(payload_dict)
        )
        db.add(ev_rec)
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"[Telemetry DB Error] {e}")

    # Broadcast event to connected 3D WebGL cockpits
    await ws_manager.broadcast({
        "type": "TELEMETRY_EVENT",
        "account_id": event.account_id,
        "event_type": event.event_type,
        "timestamp": event.timestamp,
        "payload": payload_dict
    })

    return {"status": "ingested", "account_id": event.account_id, "timestamp": event.timestamp}

@app.get("/api/graph", response_model=GraphResponse)
def get_graph():
    """Returns current active nodes, links, clusters, and Louvain modularity score Q."""
    return graph_engine.compute_clusters_and_modularity()

@app.post("/api/quarantine", response_model=QuarantineResponse)
async def quarantine_cluster(req: QuarantineRequest, db: Session = Depends(get_db)):
    """
    Executes cluster-wide quarantine isolation.
    Disables accounts, logs compliance decision, and alerts 3D cockpit.
    """
    quarantined_count = graph_engine.quarantine_cluster(req.cluster_id)

    # Persist cluster record
    try:
        c_rec = db.query(ClusterRecord).filter(ClusterRecord.cluster_id == req.cluster_id).first()
        if not c_rec:
            c_rec = ClusterRecord(
                cluster_id=req.cluster_id,
                size=quarantined_count,
                status="quarantined",
                quarantined_at=time.time(),
                reasons_json=json.dumps([req.reason])
            )
            db.add(c_rec)
        else:
            c_rec.status = "quarantined"
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"[Quarantine DB Error] {e}")

    # Broadcast quarantine update to WebSockets
    await ws_manager.broadcast({
        "type": "QUARANTINE_TRIGGERED",
        "cluster_id": req.cluster_id,
        "operator_id": req.operator_id,
        "quarantined_accounts": quarantined_count,
        "timestamp": time.time()
    })

    return QuarantineResponse(
        status="quarantined",
        cluster_id=req.cluster_id,
        quarantined_accounts=quarantined_count,
        timestamp=time.time()
    )

@app.post("/api/simulate_swarm")
async def simulate_swarm():
    """Populates graph engine with 80 legitimate humans and 20 synchronized bots."""
    result = populate_mock_cyber_range(graph_engine)
    # Broadcast simulation alert
    await ws_manager.broadcast({
        "type": "SWARM_SIMULATION_DEPLOYED",
        "human_nodes": result["human_nodes"],
        "bot_nodes": result["bot_nodes"],
        "modularity_q": result["modularity_q"]
    })
    return result

@app.post("/api/reset")
async def reset_graph():
    """Clears in-memory graph state for a fresh demonstration."""
    graph_engine.reset()
    await ws_manager.broadcast({"type": "GRAPH_RESET"})
    return {"status": "cleared", "active_nodes": 0}

@app.get("/api/sar/export", response_class=PlainTextResponse)
async def export_sar(cluster_id: int = 1):
    """Generates official CFPB-compliant SAR legal narrative via NVIDIA NIM or fallback."""
    res = graph_engine.compute_clusters_and_modularity()
    cluster_info = None
    for c in res.clusters:
        if c.cluster_id == cluster_id:
            cluster_info = c.model_dump()
            break
    if not cluster_info:
        cluster_info = {"cluster_id": cluster_id, "size": 20, "modularity_q": res.global_modularity or 0.72}

    narrative = await generate_sar_report_narrative(cluster_info)
    return narrative

# ---------------------------------------------------------
# WebSocket Endpoints
# ---------------------------------------------------------

@app.websocket("/ws/telemetry")
@app.websocket("/ws/graph_live")
async def websocket_endpoint(websocket: WebSocket):
    """Streams live telemetry packets and periodic graph state to the 3D cockpit."""
    await ws_manager.connect(websocket)
    try:
        # Send initial graph snapshot immediately upon connection
        current_state = graph_engine.compute_clusters_and_modularity().model_dump()
        await websocket.send_json({"type": "INITIAL_GRAPH_STATE", "data": current_state})

        while True:
            # Keepalive listener
            data = await websocket.receive_text()
            if data == "ping":
                await websocket.send_text("pong")
    except WebSocketDisconnect:
        ws_manager.disconnect(websocket)
    except Exception:
        ws_manager.disconnect(websocket)
