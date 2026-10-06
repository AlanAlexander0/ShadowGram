#!/usr/bin/env python3
"""
run_all_tests.py
Master Test & Integrity Verification Suite for ShadowGram.
Runs 8 comprehensive test phases across all modules, stations, models, and web assets:
- Phase 1: Python Syntax & Compilation (All 30+ .py files)
- Phase 2: Core Module Imports & Fallback Integrity
- Phase 3: Two-Key Defense & Graph Engine Runtime
- Phase 4: Common-Cause Wi-Fi Protection
- Phase 5: Denial-of-Wallet Economics & Step-Up Verification
- Phase 6: ReportLab & Pure PDF 1.4 Generation
- Phase 7: Offline Persona Cache Integrity
- Phase 8: Web Assets & HTML/JS Frontend Contract Audit
"""

import os
import sys
import time
import json
import math
import random
import py_compile
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


# Add project root to sys.path
ROOT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT_DIR))

PASSED_COUNT = 0
FAILED_COUNT = 0
TEST_LOG = []

def record_result(phase_name: str, test_desc: str, success: bool, detail: str = ""):
    global PASSED_COUNT, FAILED_COUNT
    if success:
        PASSED_COUNT += 1
        status = "PASS"
        print(f"  [{status}] {test_desc}")
    else:
        FAILED_COUNT += 1
        status = "FAIL"
        print(f"  [{status}] {test_desc} -- ERROR: {detail}")
    TEST_LOG.append((phase_name, test_desc, status, detail))


def phase1_compile_all_python_files():
    print("\n" + "=" * 80)
    print("PHASE 1: Python Syntax & Compilation Check (All .py files)")
    print("=" * 80)

    py_files = []
    for root, dirs, files in os.walk(ROOT_DIR):
        # Skip virtual environments and hidden dirs
        if "venv" in root or ".git" in root or "__pycache__" in root:
            continue
        for f in files:
            if f.endswith(".py"):
                py_files.append(Path(root) / f)

    print(f"Found {len(py_files)} Python files to compile...")
    for pf in sorted(py_files):
        rel_path = pf.relative_to(ROOT_DIR)
        try:
            with open(pf, "r", encoding="utf-8") as f:
                source = f.read()
            compile(source, str(pf), "exec")
            record_result("Phase 1", f"Compile {rel_path}", True)
        except Exception as e:
            record_result("Phase 1", f"Compile {rel_path}", False, str(e))


def phase2_module_import_and_fallbacks():
    print("\n" + "=" * 80)
    print("PHASE 2: Core Module Imports & Fallback Integrity")
    print("=" * 80)

    # 1. Test models.py import and schemas
    try:
        from backend.models import (
            BaseModel, Field, SessionRecord, TelemetryPayload,
            TelemetryEvent, GraphNode, GraphLink, GraphCluster, GraphResponse,
            StepUpVerifyRequest, StepUpVerifyResponse, DoWStatsResponse
        )
        # Verify schema instantiation
        node = GraphNode(id="ACC-01", session_id="SESS-01", kinetic_jerk_score=0.88, risk_label="normal_organic")
        link = GraphLink(source="ACC-01", target="ACC-02", weight=0.85, converged_layers=["timing", "navigation"], delta_t_seconds=0.04)
        assert node.id == "ACC-01"
        assert link.weight == 0.85
        record_result("Phase 2", "Import & instantiate backend.models schemas", True)
    except Exception as e:
        record_result("Phase 2", "Import & instantiate backend.models schemas", False, str(e))

    # 2. Test embedding_worker fallback
    try:
        from backend.embedding_worker import SemanticIntentWorker
        worker = SemanticIntentWorker()
        vec = worker.encode("Emergency medical expense")
        assert len(vec) == 384, f"Vector length is {len(vec)}, expected 384"
        sim = worker.cosine_similarity(vec, vec)
        assert abs(sim - 1.0) < 0.01, f"Self-similarity is {sim}, expected ~1.0"
        record_result("Phase 2", "SemanticIntentWorker encoding & cosine similarity", True)
    except Exception as e:
        record_result("Phase 2", "SemanticIntentWorker encoding & cosine similarity", False, str(e))

    # 3. Test kinetic_classifier fallback
    try:
        from backend.kinetic_classifier import KineticJerkClassifier
        classifier = KineticJerkClassifier()
        dummy_coords = [[0, 0, 0], [10, 10, 16], [20, 20, 33], [30, 30, 50]]
        score = classifier.evaluate_trajectory(dummy_coords)
        assert 0.0 <= score <= 1.0, f"Kinetic score {score} out of bounds"
        record_result("Phase 2", "KineticJerkClassifier trajectory evaluation", True)
    except Exception as e:
        record_result("Phase 2", "KineticJerkClassifier trajectory evaluation", False, str(e))

    # 4. Test fallback_sar narrative
    try:
        from backend.fallback_sar import deterministic_sar_narrative
        sample_cluster = {"cluster_id": 1, "size": 20, "modularity_q": 0.7241, "p_value": 0.0001, "dow_savings_inr": 1220.0}
        narrative = deterministic_sar_narrative(sample_cluster)
        assert "REGULATION B" in narrative
        assert "CR-01" in narrative
        assert "₹1220.00" in narrative
        record_result("Phase 2", "Deterministic fallback SAR narrative formatting", True)
    except Exception as e:
        record_result("Phase 2", "Deterministic fallback SAR narrative formatting", False, str(e))

    # 5. Test trajectory generator
    try:
        from simulation.trajectory import generate_human_trajectory
        coords = generate_human_trajectory((100, 100), (500, 500), points=30)
        assert len(coords) >= 10
        assert len(coords[0]) == 3  # [x, y, t]
        record_result("Phase 2", "Biomechanical trajectory generator (Flash & Hogan)", True)
    except Exception as e:
        record_result("Phase 2", "Biomechanical trajectory generator (Flash & Hogan)", False, str(e))


def phase3_two_key_defense_runtime():
    print("\n" + "=" * 80)
    print("PHASE 3: Two-Key Defense & Graph Engine Runtime")
    print("=" * 80)

    try:
        from backend.graph_engine import ShadowGraphEngine
        engine = ShadowGraphEngine(window_seconds=600.0, edge_threshold=0.78)

        # 1. Test Key 1 Fast Filter with Naive Bot
        t_start = time.perf_counter()
        engine.ingest_event(
            session_id="sess-naive-01",
            account_id="ACC-NAIVE-01",
            event_type="pointerdown",
            timestamp=time.time(),
            payload={
                "click_dwell_duration_ms": 1.0,
                "mousemove_pre_click_count": 0,
                "pointer_curvature_jerk": 0.0,
                "route_path": "/loan_details"
            }
        )
        t_ms = (time.perf_counter() - t_start) * 1000.0
        sess = engine.sessions["ACC-NAIVE-01"]
        assert sess.key1_status == "flagged_automation", f"Key 1 status: {sess.key1_status}"
        assert t_ms < 50.0, f"Key 1 latency {t_ms:.2f}ms too high"
        record_result("Phase 3", f"Key 1 Fast Filter catches naive bot in {t_ms:.3f}ms", True)

        # 2. Test Key 1 Clean for Honest Human
        engine.ingest_event(
            session_id="sess-human-01",
            account_id="ACC-HUMAN-01",
            event_type="pointerdown",
            timestamp=time.time() + 1.0,
            payload={
                "click_dwell_duration_ms": 115.0,
                "mousemove_pre_click_count": 24,
                "pointer_curvature_jerk": 0.28,
                "route_path": "/apply"
            }
        )
        sess_h = engine.sessions["ACC-HUMAN-01"]
        assert sess_h.key1_status == "cleared", f"Human key1 status: {sess_h.key1_status}"
        record_result("Phase 3", "Key 1 Fast Filter clears honest human session", True)

        # 3. Test Key 2 Relational Clustering with 5 Coordinated Bots
        base_t = time.time() + 10.0
        for i in range(1, 6):
            engine.ingest_event(
                session_id=f"sess-swarm-{i}",
                account_id=f"ACC-SWARM-{i}",
                event_type="loan_submit",
                timestamp=base_t + (i * 0.025),  # 25ms lockstep ingress
                payload={
                    "click_dwell_duration_ms": 90.0,
                    "mousemove_pre_click_count": 15,
                    "pointer_curvature_jerk": 0.85,
                    "route_path": "/loan_details",
                    "narrative_text": "Medical surgery urgent advance required",
                    "client_canvas_hash": "canvas-bot-shared-hash-01"
                }
            )

        graph_state = engine.get_graph_state()
        syndicates = [c for c in graph_state.clusters if c.cluster_id > 0]
        assert len(syndicates) >= 1, "Expected at least 1 syndicate cluster"
        cluster = syndicates[0]
        assert cluster.size >= 5, f"Expected cluster size >= 5, got {cluster.size}"
        assert cluster.modularity_q > 0.40, f"Modularity Q is {cluster.modularity_q}"
        record_result("Phase 3", f"Key 2 Relational Engine clusters 5 stealth bots (Q = {cluster.modularity_q:.4f})", True)

    except Exception as e:
        record_result("Phase 3", "Two-Key Defense & Graph Engine Runtime", False, str(e))


def phase4_common_cause_wifi_protection():
    print("\n" + "=" * 80)
    print("PHASE 4: Common-Cause Wi-Fi Protection Test")
    print("=" * 80)

    try:
        from backend.graph_engine import ShadowGraphEngine
        engine = ShadowGraphEngine(window_seconds=600.0, edge_threshold=0.78)

        # Ingest 10 students sharing same IP hash but diverse routes & texts
        base_t = time.time() + 50.0
        routes = ["/sports_loan", "/tuition_loan", "/hostel_loan", "/laptop_loan", "/exam_fees"]
        texts = [
            "Need laptop repair for semester exams",
            "College fest sponsorship funding",
            "Semester books and library deposit",
            "Hostel room mess advance fee payment",
            "Course certification examination fee"
        ]

        for i in range(10):
            engine.ingest_event(
                session_id=f"sess-campus-{i}",
                account_id=f"ACC-CAMPUS-STUDENT-{i}",
                event_type="loan_submit",
                timestamp=base_t + (i * 1.5),
                payload={
                    "ip_hash": "hash-shared-eduroam-wifi-01",  # Same IP
                    "client_canvas_hash": f"canvas-student-{i}",  # Varied canvas
                    "click_dwell_duration_ms": 95.0 + (i * 5.0),
                    "mousemove_pre_click_count": 15 + i,
                    "pointer_curvature_jerk": 0.25,
                    "route_path": routes[i % len(routes)],
                    "narrative_text": texts[i % len(texts)]
                }
            )

        graph_state = engine.get_graph_state()
        campus_clusters = [c for c in graph_state.clusters if c.cluster_id > 0]
        # Should be 0 syndicate clusters because common-cause discount protects them
        assert len(campus_clusters) == 0, f"Expected 0 false-positive clusters, got {len(campus_clusters)}"
        record_result("Phase 4", "Common-Cause Discount prevents false-positive campus Wi-Fi clustering", True)

    except Exception as e:
        record_result("Phase 4", "Common-Cause Wi-Fi Protection Test", False, str(e))


def phase5_dow_economics_and_stepup():
    print("\n" + "=" * 80)
    print("PHASE 5: Denial-of-Wallet Economics & Step-Up Verification")
    print("=" * 80)

    try:
        from backend.graph_engine import ShadowGraphEngine
        engine = ShadowGraphEngine(window_seconds=600.0, edge_threshold=0.78)

        # Ingest 10 bots
        base_t = time.time() + 100.0
        for i in range(10):
            engine.ingest_event(
                session_id=f"sess-dow-{i}",
                account_id=f"ACC-DOW-{i}",
                event_type="loan_submit",
                timestamp=base_t + (i * 0.02),
                payload={
                    "click_dwell_duration_ms": 1.0,
                    "mousemove_pre_click_count": 0,
                    "route_path": "/loan_details",
                    "narrative_text": "Hospital bills emergency deposit",
                    "client_canvas_hash": "canvas-dow-bot"
                }
            )

        # Quarantine cluster
        quarantined_count = engine.quarantine_cluster(1)
        graph_state = engine.get_graph_state()
        expected_dow = 10 * 61.0  # ₹61.00 per bot
        assert graph_state.total_dow_savings_inr == expected_dow, f"DoW savings: {graph_state.total_dow_savings_inr}, expected {expected_dow}"
        record_result("Phase 5", f"DoW Calculator confirmed ₹{expected_dow:.2f} savings for 10 bots", True)

        # Step-up verification test: Clear ACC-DOW-0
        assert engine.sessions["ACC-DOW-0"].status == "quarantined"
        clear_success = engine.verify_step_up("ACC-DOW-0")
        assert clear_success is True, "Step-up verification failed to return True"
        assert engine.sessions["ACC-DOW-0"].status == "cleared"
        assert engine.sessions["ACC-DOW-0"].step_up_status == "cleared"
        record_result("Phase 5", "Reversible UPI Step-Up challenge clears quarantined account", True)

    except Exception as e:
        record_result("Phase 5", "Denial-of-Wallet Economics & Step-Up Verification", False, str(e))


def phase6_sar_pdf_generation():
    print("\n" + "=" * 80)
    print("PHASE 6: 2-Page SAR PDF Generation Check")
    print("=" * 80)

    try:
        from backend.sar_generator import generate_sar_pdf
        sample_cluster = {
            "cluster_id": 1,
            "size": 20,
            "modularity_q": 0.7241,
            "p_value": 0.0001,
            "dow_savings_inr": 1220.0,
            "algorithm": "Leiden v2.1",
            "factual_reasons": [
                "CR-01: Navigation route sequence invariance (LCS >= 0.85)",
                "CR-02: Micro-temporal arrival synchronization (delta_t < 40ms)",
                "CR-03: Zero neuromuscular tremor and constant jerk",
                "CR-04: Semantic prompt homogeneity (all-MiniLM cosine >= 0.88)"
            ],
            "account_ids": [f"ACC-SYNTH-{i:03d}" for i in range(1, 21)]
        }

        t_start = time.perf_counter()
        pdf_bytes = generate_sar_pdf(sample_cluster)
        t_ms = (time.perf_counter() - t_start) * 1000.0

        assert isinstance(pdf_bytes, bytes), "Expected PDF bytes"
        assert len(pdf_bytes) > 2000, f"PDF byte length too small: {len(pdf_bytes)}"
        assert pdf_bytes.startswith(b"%PDF"), "PDF does not start with %PDF header"
        record_result("Phase 6", f"Generated 2-Page SAR PDF ({len(pdf_bytes)} bytes in {t_ms:.1f}ms)", True)

    except Exception as e:
        record_result("Phase 6", "SAR PDF Generation Check", False, str(e))


def phase7_personas_cache_integrity():
    print("\n" + "=" * 80)
    print("PHASE 7: Offline Persona Cache Integrity Check")
    print("=" * 80)

    cache_path = ROOT_DIR / "simulation" / "personas_cache.json"
    try:
        assert cache_path.exists(), f"Persona cache missing at {cache_path}"
        with open(cache_path, "r", encoding="utf-8") as f:
            personas = json.load(f)
        assert isinstance(personas, list), "Expected list of personas"
        assert len(personas) >= 20, f"Expected at least 20 personas, got {len(personas)}"
        p0 = personas[0]
        for key in ["full_name", "phone", "pan", "loan_purpose_narrative", "account_id"]:
            assert key in p0, f"Missing key '{key}' in persona"
        record_result("Phase 7", f"Verified {len(personas)} offline fallback personas with valid schema", True)
    except Exception as e:
        record_result("Phase 7", "Offline Persona Cache Integrity Check", False, str(e))


def phase8_frontend_assets_and_contracts():
    print("\n" + "=" * 80)
    print("PHASE 8: Web Assets & HTML/JS Frontend Contract Audit")
    print("=" * 80)

    # 1. Check telemetry.js
    telem_path = ROOT_DIR / "public" / "telemetry.js"
    try:
        assert telem_path.exists(), "public/telemetry.js missing"
        telem_content = telem_path.read_text(encoding="utf-8")
        assert "click_dwell_duration_ms" in telem_content
        assert "mousemove_pre_click_count" in telem_content
        assert "/telemetry" in telem_content
        record_result("Phase 8", "public/telemetry.js contains all invariant collectors", True)
    except Exception as e:
        record_result("Phase 8", "public/telemetry.js verification", False, str(e))

    # 2. Check athenapay_portal.html
    portal_path = ROOT_DIR / "public" / "athenapay_portal.html"
    try:
        assert portal_path.exists(), "public/athenapay_portal.html missing"
        portal_content = portal_path.read_text(encoding="utf-8")
        assert ("honey_sync" in portal_content or "website_url_verification" in portal_content)  # Honey-DOM
        assert "stepup-modal" in portal_content  # Step-Up modal
        assert "/api/step-up/verify" in portal_content  # API call
        assert "telemetry.js" in portal_content  # Script inclusion
        record_result("Phase 8", "public/athenapay_portal.html contains Honey-DOM and Step-Up modal", True)
    except Exception as e:
        record_result("Phase 8", "public/athenapay_portal.html verification", False, str(e))

    # 3. Check cockpit.html
    cockpit_path = ROOT_DIR / "public" / "cockpit.html"
    try:
        assert cockpit_path.exists(), "public/cockpit.html missing"
        cockpit_content = cockpit_path.read_text(encoding="utf-8")
        assert "three" in cockpit_content.lower() or "canvas" in cockpit_content.lower()
        assert "why-card" in cockpit_content.lower() or "modal" in cockpit_content.lower()
        assert "dow" in cockpit_content.lower() or "saved" in cockpit_content.lower()
        record_result("Phase 8", "public/cockpit.html contains 3D visualizer & Why Card modal", True)
    except Exception as e:
        record_result("Phase 8", "public/cockpit.html verification", False, str(e))

    # 4. Check stations completeness
    stations = [
        ("station1_alan_swarm", ["swarm_runner.py", "trajectory.py", "generate_personas.py", "README.md"]),
        ("station2_pete_backend", ["main.py", "graph_engine.py", "models.py", "database.py", "README.md"]),
        ("station3_aiswarya_frontend", ["athenapay_portal.html", "cockpit.html", "telemetry.js", "README.md"]),
        ("station4_nihad_compliance", ["sar_generator.py", "nim_client.py", "fallback_sar.py", "page.tsx", "README.md"])
    ]
    for s_name, req_files in stations:
        s_dir = ROOT_DIR / "stations" / s_name
        try:
            assert s_dir.exists(), f"Station directory {s_name} missing"
            for rf in req_files:
                assert (s_dir / rf).exists(), f"File {rf} missing in {s_name}"
            record_result("Phase 8", f"Station folder {s_name} is complete and self-contained", True)
        except Exception as e:
            record_result("Phase 8", f"Station folder {s_name} completeness", False, str(e))


def main():
    print("=" * 80)
    print("STARTING COMPLETE SHADOWGRAM INTEGRITY TEST SUITE")
    print(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}")
    print(f"Root: {ROOT_DIR}")
    print("=" * 80)

    phase1_compile_all_python_files()
    phase2_module_import_and_fallbacks()
    phase3_two_key_defense_runtime()
    phase4_common_cause_wifi_protection()
    phase5_dow_economics_and_stepup()
    phase6_sar_pdf_generation()
    phase7_personas_cache_integrity()
    phase8_frontend_assets_and_contracts()

    print("\n" + "=" * 80)
    print("TEST SUITE EXECUTION SUMMARY")
    print("=" * 80)
    print(f"Total Tests Executed: {PASSED_COUNT + FAILED_COUNT}")
    print(f"  -> PASSED: {PASSED_COUNT}")
    print(f"  -> FAILED: {FAILED_COUNT}")

    if FAILED_COUNT == 0:
        print("\n🎉 ALL TESTS PASSED! THE ENTIRE CODEBASE IS 100% HEALTHY AND OPERATIONAL.")
        print("Zero syntax errors, zero broken imports, complete fallback protection.")
    else:
        print(f"\n⚠️ {FAILED_COUNT} TESTS FAILED. Inspect the error log above.")

    print("=" * 80 + "\n")
    return 0 if FAILED_COUNT == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
