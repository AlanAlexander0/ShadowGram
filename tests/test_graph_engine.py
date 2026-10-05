import pytest
import time
from backend.graph_engine import ShadowGraphEngine

def test_shadow_graph_engine_initialization():
    engine = ShadowGraphEngine(window_seconds=600.0, edge_threshold=0.78)
    assert engine.graph.number_of_nodes() == 0
    assert engine.graph.number_of_edges() == 0

def test_single_human_session_ingestion():
    engine = ShadowGraphEngine()
    now = time.time()
    payload = {
        "route_path": "/apply",
        "key_flight_time_ms": 120.0,
        "key_dwell_time_ms": 65.0,
        "pointer_curvature_jerk": 0.15,
        "narrative_text": "Medical emergency fee for hospital bill",
        "client_canvas_hash": "hash-human-1"
    }
    engine.ingest_event("sess-1", "HUMAN-01", "loan_submit", now, payload)
    assert "HUMAN-01" in engine.sessions
    assert engine.graph.has_node("HUMAN-01")

def test_pairwise_sparsification_filter():
    """Verify that 2 independent humans sharing only typing speed are NOT linked."""
    engine = ShadowGraphEngine()
    t = time.time()

    # Human A
    engine.ingest_event("sess-a", "HUMAN-A", "loan_submit", t, {
        "route_path": "/products",
        "key_flight_time_ms": 100.0,
        "narrative_text": "Need loan for new camera lens",
        "client_canvas_hash": "hash-a"
    })

    # Human B (different time, route, text, canvas)
    engine.ingest_event("sess-b", "HUMAN-B", "loan_submit", t + 45.0, {
        "route_path": "/calculator",
        "key_flight_time_ms": 102.0,
        "narrative_text": "Repair vehicle clutch plate",
        "client_canvas_hash": "hash-b"
    })

    # They should NOT have an edge (sparsification filter prunes)
    assert not engine.graph.has_edge("HUMAN-A", "HUMAN-B")

def test_syndicate_cluster_detection():
    """Verify that 5 synchronized bots matching across 4 layers form a high-Q cluster."""
    engine = ShadowGraphEngine()
    burst_time = time.time()
    shared_canvas = "syndicate-canvas-hash"
    fsm = ["/auth", "/kyc", "/submit"]

    for i in range(1, 6):
        bot_id = f"BOT-{i}"
        engine.ingest_event(f"sess-bot-{i}", bot_id, "loan_submit", burst_time + (i * 0.002), {
            "route_path": "/submit",
            "key_flight_time_ms": 50.0,
            "key_dwell_time_ms": 30.0,
            "pointer_curvature_jerk": 0.95,
            "narrative_text": "Emergency micro loan for appliance repair maintenance",
            "client_canvas_hash": shared_canvas
        })
        engine.sessions[bot_id].routes = fsm

    for i in range(1, 6):
        engine.recompute_node_edges(f"BOT-{i}")

    res = engine.compute_clusters_and_modularity()
    assert len(res.clusters) >= 1
    assert res.clusters[0].size == 5
    assert res.clusters[0].modularity_q > 0.30
