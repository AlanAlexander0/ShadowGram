import pytest
import time
from fastapi.testclient import TestClient
from backend.main import app, graph_engine

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "online"
    assert data["service"] == "ShadowGram Core Engine"

def test_telemetry_ingest():
    payload = {
        "session_id": "test-session-uuid-001",
        "account_id": "ACC-TEST-99",
        "timestamp": time.time(),
        "event_type": "keydown",
        "payload": {
            "key_flight_time_ms": 42.5,
            "key_dwell_time_ms": 68.0,
            "pointer_curvature_jerk": 0.12,
            "route_path": "/apply"
        }
    }
    response = client.post("/telemetry", json=payload)
    assert response.status_code == 200
    assert response.json()["status"] == "ingested"
    assert response.json()["account_id"] == "ACC-TEST-99"

def test_graph_endpoint():
    response = client.get("/api/graph")
    assert response.status_code == 200
    data = response.json()
    assert "nodes" in data
    assert "links" in data
    assert "clusters" in data
    assert "global_modularity" in data

def test_simulation_swarm():
    response = client.post("/api/simulate_swarm")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["bot_nodes"] == 20
    assert data["human_nodes"] == 80
    assert data["modularity_q"] > 0.30

    # Query graph after simulation
    graph_res = client.get("/api/graph").json()
    assert len(graph_res["nodes"]) >= 100
    assert len(graph_res["clusters"]) >= 1

def test_quarantine_cluster():
    # Quarantine cluster 1
    req = {
        "cluster_id": 1,
        "action": "isolate",
        "reason": "Coordinated synthetic bot swarm detected via Louvain community clustering",
        "operator_id": "OFFICER-TEST"
    }
    response = client.post("/api/quarantine", json=req)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "quarantined"
    assert data["cluster_id"] == 1

def test_sar_export():
    response = client.get("/api/sar/export?cluster_id=1")
    assert response.status_code == 200
    text = response.text
    assert "FINANCIAL CRIMES ENFORCEMENT & ADVERSE ACTION COMPLIANCE REPORT" in text
    assert "CFPB CIRCULAR 2023-03" in text
    assert "REASON CODE" in text

def test_reset():
    response = client.post("/api/reset")
    assert response.status_code == 200
    data = client.get("/api/graph").json()
    assert len(data["nodes"]) == 0
