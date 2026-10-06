import time
import random
from typing import Dict, Any

try:
    from graph_engine import ShadowGraphEngine
except ImportError:
    from backend.graph_engine import ShadowGraphEngine

HUMAN_NARRATIVES = [
    "Need urgent assistance for my mother hospital admission and cardiology checkup.",
    "Purchasing a used laptop for my online coding bootcamp classes this semester.",
    "Emergency roof repair after unexpected monsoon rains damaged our kitchen.",
    "Advance payment for college hostel fees and semester examination registration.",
    "Purchasing seed fertilizers and diesel pump parts for agricultural harvesting.",
    "Two-wheeler vehicle insurance renewal and battery replacement fee.",
    "Small business shop inventory restocking for upcoming festival season.",
    "Dental root canal treatment and prescription medicines for grandmother."
]

BOT_NARRATIVES = [
    "Immediate emergency micro-loan required for urgent appliance maintenance expenses.",
    "Urgent personal micro-loan required for immediate appliance repair expenditures.",
    "Immediate emergency micro-loan required for unexpected appliance repair costs.",
    "Urgent personal micro-loan needed for urgent household repair bills.",
    "Immediate financial micro-loan required for appliance servicing emergency.",
    "Urgent personal micro-loan needed for immediate domestic appliance servicing.",
    "Immediate micro-loan needed for urgent household maintenance expenditures.",
    "Urgent personal micro-loan required for immediate appliance repair bills."
]

def populate_mock_cyber_range(engine: ShadowGraphEngine) -> Dict[str, Any]:
    """
    Populates the engine with 80 scattered organic human sessions
    and 20 phase-locked, synchronized AI bot accounts.
    Guarantees instant demo recovery if venue Wi-Fi drops.
    """
    engine.reset()
    base_time = time.time() - 300.0

    # 1. Ingest 80 Legitimate Human Sessions
    for i in range(1, 81):
        acc_id = f"HUMAN-{1000 + i}"
        session_id = f"sess-human-{i}"
        t_arr = base_time + random.uniform(0.0, 280.0)
        routes = ["/home", "/products", "/calculator", "/apply"] if i % 2 == 0 else ["/promo", "/apply", "/terms"]
        human_jerk = random.uniform(0.08, 0.28)
        
        payload = {
            "route_path": routes[-1],
            "key_flight_time_ms": random.uniform(80.0, 320.0),
            "key_dwell_time_ms": random.uniform(40.0, 140.0),
            "pointer_curvature_jerk": human_jerk,
            "narrative_text": random.choice(HUMAN_NARRATIVES),
            "client_canvas_hash": f"canvas-hash-{i % 15}"
        }
        
        engine.ingest_event(session_id, acc_id, "loan_submit", t_arr, payload)
        if acc_id in engine.sessions:
            engine.sessions[acc_id].routes = routes

    # 2. Ingest 20 Coordinated AI Bots
    burst_start = time.time() - 15.0
    fsm_path = ["/auth", "/kyc", "/loan_details", "/submit"]
    shared_canvas = "a8f3b92c4e1d5a77"

    for j in range(1, 21):
        bot_acc_id = f"BOT-{89400 + j}"
        bot_sess_id = f"sess-bot-swarm-{j}"
        t_bot = burst_start + (j * 0.0019)
        bot_jerk = random.uniform(0.94, 0.98)
        
        bot_payload = {
            "route_path": "/submit",
            "key_flight_time_ms": 50.0 + random.uniform(-0.5, 0.5),
            "key_dwell_time_ms": 30.0 + random.uniform(-0.5, 0.5),
            "pointer_curvature_jerk": bot_jerk,
            "narrative_text": random.choice(BOT_NARRATIVES),
            "client_canvas_hash": shared_canvas
        }
        
        engine.ingest_event(bot_sess_id, bot_acc_id, "loan_submit", t_bot, bot_payload)
        if bot_acc_id in engine.sessions:
            engine.sessions[bot_acc_id].routes = fsm_path

    # Force recompute edges for all bots
    for j in range(1, 21):
        engine.recompute_node_edges(f"BOT-{89400 + j}")

    res = engine.compute_clusters_and_modularity()
    return {
        "status": "success",
        "human_nodes": 80,
        "bot_nodes": 20,
        "modularity_q": res.global_modularity,
        "clusters_detected": len(res.clusters),
        "cluster_size": res.clusters[0].size if res.clusters else 0
    }
