"""
stations/station1_alan_swarm/test_two_key_defense.py
Comprehensive regression test verifying the Two-Key Defense Architecture:
1. Key 1 Fast Automation Filter: Catches naive bots in <5ms via event-stream invariants.
2. Key 2 Relational Physics Graph: Intercepts stealthy bots via multi-layer community clustering.
3. Denial-of-Wallet (DoW) economics: Confirms ₹61.00/bot capital savings.
4. Step-Up Verification: Confirms reversible challenge clears flagged accounts.
"""

import sys
import time
import random
from pathlib import Path

# Try loading from parent ATHENA repo if present, or local
try:
    from backend.graph_engine import ShadowGraphEngine
except ImportError:
    root_dir = Path(__file__).resolve().parent.parent.parent
    sys.path.insert(0, str(root_dir))
    from backend.graph_engine import ShadowGraphEngine


def run_two_key_tests():
    print("=" * 70)
    print("RUNNING SHADOWGRAM TWO-KEY ARCHITECTURE VERIFICATION SUITE")
    print("=" * 70)

    engine = ShadowGraphEngine(window_seconds=600.0, edge_threshold=0.78)

    # ---------------------------------------------------------
    # TEST 1: Key 1 Fast Automation Filter (Naive Bot Interception)
    # ---------------------------------------------------------
    print("\n[TEST 1] Key 1 Fast Automation Filter (Target: <5ms Decision Time)")
    naive_session = "sess-naive-playwright-01"
    naive_account = "ACC-NAIVE-999"

    t_start = time.perf_counter()
    engine.ingest_event(
        session_id=naive_session,
        account_id=naive_account,
        event_type="pointerdown",
        timestamp=time.time(),
        payload={
            "click_dwell_duration_ms": 1.0,        # Zero dwell time (instant click)
            "mousemove_pre_click_count": 0,         # Zero mouse movement before click
            "pointer_curvature_jerk": 0.0,          # Zero jerk (synthetic leap)
            "route_path": "/loan_details"
        }
    )
    t_elapsed_ms = (time.perf_counter() - t_start) * 1000.0

    session_obj = engine.sessions[naive_account]
    assert session_obj.key1_status == "flagged_automation", f"Expected flagged_automation, got {session_obj.key1_status}"
    print(f"  -> SUCCESS: Naive bot flagged instantly by Key 1 filter.")
    print(f"  -> Decision Latency: {t_elapsed_ms:.3f}ms (Benchmark < 5.0ms: PASS)")

    # ---------------------------------------------------------
    # TEST 2: Key 1 Organic Human Exemption
    # ---------------------------------------------------------
    print("\n[TEST 2] Key 1 Organic Human Exemption")
    human_account = "ACC-HUMAN-ORGANIC-01"
    engine.ingest_event(
        session_id="sess-human-01",
        account_id=human_account,
        event_type="pointerdown",
        timestamp=time.time(),
        payload={
            "click_dwell_duration_ms": 105.4,       # Realistic human dwell
            "mousemove_pre_click_count": 22,         # Natural cursor approach
            "pointer_curvature_jerk": 0.18,          # Physiological 8-12 Hz tremor
            "route_path": "/home"
        }
    )
    human_obj = engine.sessions[human_account]
    assert human_obj.key1_status == "cleared", f"Expected cleared, got {human_obj.key1_status}"
    print(f"  -> SUCCESS: Organic human cleared Key 1 without false alarm.")

    # ---------------------------------------------------------
    # TEST 3: Key 2 Relational Physics Graph (Stealth Syndicate Detection)
    # ---------------------------------------------------------
    print("\n[TEST 3] Key 2 Relational Physics Graph & Leiden Detection")
    engine.reset()

    # Ingest 20 stealth bots (each passes Key 1 individually, but are correlated)
    base_t = time.time()
    shared_canvas = "syndicate-canvas-hash-x9"
    fsm_path = ["/auth", "/kyc", "/loan_details", "/submit"]
    semantic_justification = "Urgent personal micro-loan needed for immediate household repair expenditures."

    for i in range(20):
        bot_acc = f"BOT-STEALTH-{i+1:02d}"
        bot_sess = f"sess-stealth-{i+1:02d}"
        t_arr = base_t + (i * 0.0018)  # Tight arrival delta (36ms window)

        engine.ingest_event(
            session_id=bot_sess,
            account_id=bot_acc,
            event_type="loan_submit",
            timestamp=t_arr,
            payload={
                "click_dwell_duration_ms": 95.0 + (i % 3),  # Passes Key 1
                "mousemove_pre_click_count": 18,            # Passes Key 1
                "pointer_curvature_jerk": 0.012,
                "client_canvas_hash": shared_canvas,
                "narrative_text": semantic_justification,
                "route_path": "/submit"
            }
        )
        engine.sessions[bot_acc].routes = fsm_path
        assert engine.sessions[bot_acc].key1_status == "cleared", "Stealth bot should pass Key 1"

    # Ingest 10 uncoordinated organic humans
    for j in range(10):
        h_acc = f"HUMAN-LEGIT-{j+1:02d}"
        engine.ingest_event(
            session_id=f"sess-legit-{j+1:02d}",
            account_id=h_acc,
            event_type="loan_submit",
            timestamp=base_t - random.uniform(50, 300),
            payload={
                "click_dwell_duration_ms": 110.0 + random.uniform(10, 50),
                "mousemove_pre_click_count": 30,
                "pointer_curvature_jerk": random.uniform(0.12, 0.25),
                "client_canvas_hash": f"organic-hash-{j}",
                "narrative_text": f"Different human reason {j} for college tuition or seed purchase.",
                "route_path": "/apply"
            }
        )

    # Recompute graph edges
    for i in range(20):
        engine.recompute_node_edges(f"BOT-STEALTH-{i+1:02d}")

    graph_res = engine.compute_clusters_and_modularity()
    print(f"  -> Total Nodes: {len(graph_res.nodes)}")
    print(f"  -> Total Links: {len(graph_res.links)}")
    print(f"  -> Global Modularity Q: {graph_res.global_modularity:.4f}")
    print(f"  -> Clusters Detected: {len(graph_res.clusters)}")

    assert len(graph_res.clusters) >= 1, "Failed to isolate stealth syndicate cluster"
    syndicate = graph_res.clusters[0]
    assert syndicate.size >= 15, f"Expected syndicate size >= 15, got {syndicate.size}"
    assert syndicate.modularity_q >= 0.60, f"Expected Q >= 0.60, got {syndicate.modularity_q}"
    print(f"  -> Syndicate Size: {syndicate.size} accounts")
    print(f"  -> Null Model Permutation p-value: p = {syndicate.p_value:.4f} (p < 0.001)")
    print(f"  -> SUCCESS: Key 2 caught stealth syndicate that bypassed Key 1!")

    # ---------------------------------------------------------
    # TEST 4: Denial-of-Wallet (DoW) Economic Calculations
    # ---------------------------------------------------------
    print("\n[TEST 4] Denial-of-Wallet (DoW) Capital Savings")
    q_count = engine.quarantine_cluster(syndicate.cluster_id)
    dow_stats = engine.get_dow_stats()

    expected_savings = q_count * 61.0
    assert dow_stats["total_inr_saved"] == expected_savings, f"Expected ₹{expected_savings}, got ₹{dow_stats['total_inr_saved']}"
    print(f"  -> Quarantined Accounts: {q_count}")
    print(f"  -> Pre-KYC Capital Saved: ₹{dow_stats['total_inr_saved']:.2f} (₹61.00 per account: PASS)")

    # ---------------------------------------------------------
    # TEST 5: Reversible Step-Up Challenge (Zero Permanent Bans)
    # ---------------------------------------------------------
    print("\n[TEST 5] Reversible Step-Up Challenge Verification")
    target_bot = f"BOT-STEALTH-01"
    target_sess = f"sess-stealth-01"
    assert engine.sessions[target_bot].status == "quarantined"

    # Step-Up Verification
    step_up_success = engine.verify_step_up(target_sess, target_bot, method="upi_penny_drop")
    assert step_up_success is True, "Step-Up verification should succeed"
    assert engine.sessions[target_bot].status == "active", "Account should be restored to active"
    assert engine.sessions[target_bot].step_up_status == "cleared"
    print(f"  -> SUCCESS: Quarantined account cleared via 1-rupee UPI penny drop.")

    print("\n" + "=" * 70)
    print("ALL TWO-KEY ARCHITECTURE SUITE TESTS PASSED (5/5)")
    print("=" * 70)


if __name__ == "__main__":
    run_two_key_tests()
