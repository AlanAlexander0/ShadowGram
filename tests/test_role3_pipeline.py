"""
tests/test_role3_pipeline.py - Verification Suite for Role 3 Deliverables
Assignee: Alan E Alexander (Role 3: Red-Team Swarm Runner & Client Telemetry Lead)
Document Code: SG-PROTO-00 / Quality Gate M1 & M4
"""

import asyncio
import hashlib
import hmac
import json
import re
import socket
import sys
import threading
import time
import unittest
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

# Add project root to sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from simulation.trajectory import generate_human_trajectory
from simulation.generate_personas import generate_offline_personas
from simulation.swarm_runner import compute_telemetry_hmac, SESSION_SALT


class MockTelemetryHandler(BaseHTTPRequestHandler):
    received_packets = []
    lock = threading.Lock()

    def do_POST(self):
        if self.path == "/telemetry":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length).decode("utf-8")
            data = json.loads(body)
            with self.lock:
                MockTelemetryHandler.received_packets.append(data)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"status": "ok", "ingested": true}')
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        # Suppress server request logging during test execution
        pass


class TestRole3RedTeamAndTelemetry(unittest.TestCase):

    def test_01_minimum_jerk_trajectory_generation(self):
        """Verifies Flash & Hogan biological trajectory engine."""
        p0 = (50.0, 50.0)
        p3 = (500.0, 400.0)
        waypoints = generate_human_trajectory(p0, p3, duration=0.6, fps=60)

        self.assertGreaterEqual(len(waypoints), 20, "Should generate at least 20 trajectory waypoints")
        first_pt = waypoints[0]
        last_pt = waypoints[-1]

        # Starting waypoint should be close to p0
        self.assertAlmostEqual(first_pt[0], p0[0], delta=2.0)
        self.assertAlmostEqual(first_pt[1], p0[1], delta=2.0)
        self.assertEqual(first_pt[2], 0.0)

        # Final waypoint should converge to target p3
        self.assertAlmostEqual(last_pt[0], p3[0], delta=3.0)
        self.assertAlmostEqual(last_pt[1], p3[1], delta=3.0)
        self.assertGreater(last_pt[2], 0.5)

    def test_02_personas_cache_integrity(self):
        """Verifies 20 cached personas match banking KYC requirements."""
        cache_path = PROJECT_ROOT / "simulation" / "personas_cache.json"
        self.assertTrue(cache_path.exists(), "personas_cache.json must exist")

        with open(cache_path, "r", encoding="utf-8") as f:
            personas = json.load(f)

        self.assertGreaterEqual(len(personas), 20, "Must contain at least 20 personas")
        pan_regex = re.compile(r"^[A-Z]{5}[0-9]{4}[A-Z]$")

        for p in personas[:20]:
            self.assertTrue(pan_regex.match(p["pan"]), f"Invalid PAN format: {p['pan']}")
            self.assertTrue(p["full_name"], "Persona must have a full name")
            self.assertTrue(p["loan_purpose_narrative"], "Persona must have a loan narrative")
            self.assertGreater(p["requested_loan_inr"], 0, "Requested loan must be positive")

    def test_03_telemetry_schema_and_hmac_signing(self):
        """Verifies HMAC signature generation against global session salt."""
        session_id = "test-session-uuid-1234"
        timestamp = 1741234567.890
        computed_hmac = compute_telemetry_hmac(session_id, timestamp, salt=SESSION_SALT)

        # Re-derive independently
        expected = hmac.new(
            SESSION_SALT.encode("utf-8"),
            f"{session_id}:{timestamp:.3f}".encode("utf-8"),
            hashlib.sha256
        ).hexdigest()

        self.assertEqual(computed_hmac, expected, "HMAC signature mismatch")
        self.assertEqual(len(computed_hmac), 64, "SHA-256 HMAC must be 64 hex characters")

    def test_04_end_to_end_mock_telemetry_ingress(self):
        """Spins up a local HTTP server and executes swarm_runner in direct mode."""
        # Find available port
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(("127.0.0.1", 0))
            port = s.getsockname()[1]

        MockTelemetryHandler.received_packets.clear()
        server = HTTPServer(("127.0.0.1", port), MockTelemetryHandler)
        server_thread = threading.Thread(target=server.serve_forever, daemon=True)
        server_thread.start()

        time.sleep(0.1)

        # Run direct swarm with 5 bots against mock server
        from simulation.swarm_runner import run_direct_swarm, load_personas
        personas = load_personas(PROJECT_ROOT / "simulation" / "personas_cache.json", count=5)

        telemetry_url = f"http://127.0.0.1:{port}/telemetry"
        results = asyncio.run(run_direct_swarm(personas, telemetry_url=telemetry_url, burst_window=0.5))

        # Give background HTTP threads 500ms to finish
        time.sleep(0.5)
        server.shutdown()

        self.assertEqual(len(results), 5, "Should successfully dispatch 5 bots")
        with MockTelemetryHandler.lock:
            ingested = list(MockTelemetryHandler.received_packets)

        self.assertGreater(len(ingested), 0, "Mock server should receive telemetry packets")

        # Validate schema of ingested packet
        sample = ingested[0]
        self.assertIn("session_id", sample)
        self.assertIn("account_id", sample)
        self.assertIn("timestamp", sample)
        self.assertIn("event_type", sample)
        self.assertIn("telemetry_hmac", sample)
        self.assertIn("payload", sample)


if __name__ == "__main__":
    unittest.main(verbosity=2)
