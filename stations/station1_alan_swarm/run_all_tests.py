#!/usr/bin/env python3
"""
stations/station1_alan_swarm/run_all_tests.py
Master Test & Integrity Verification Suite for ShadowGram Station 1 (Alan E Alexander).

Runs:
1. Station 1 Phase 2 & NVIDIA NIM GenAI Verification Suite (test_station1_phase2.py)
2. Two-Key Defense Architecture & Fast Filter Interception (test_two_key_defense.py)
3. ShadowGram Master Integrity Suite (run_all_tests.py)
"""

import os
import sys
from pathlib import Path

station_dir = Path(__file__).resolve().parent
root_dir = station_dir.parent.parent
sys.path.insert(0, str(root_dir))
sys.path.insert(0, str(station_dir))

import importlib.util

from test_station1_phase2 import main as run_station1_phase2
from test_two_key_defense import run_two_key_tests

spec = importlib.util.spec_from_file_location("root_run_all_tests", str(root_dir / "run_all_tests.py"))
root_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(root_module)
run_master_tests = root_module.main


def main():
    print("=" * 80)
    print("STARTING COMPLETE STATION 1 & SHADOWGRAM VERIFICATION SUITE")
    print("Station: Station 1 (Alan E Alexander - Swarm Red Team & Telemetry)")
    print("=" * 80)

    # 1. Run Station 1 & Phase 2 Specific Suite (includes NVIDIA NIM GenAI, Poisson Jitter, Digraphs)
    rc1 = run_station1_phase2()
    if rc1 != 0:
        print("\n[ERROR] Station 1 Phase 2 Suite encountered failures.")
        return rc1

    # 2. Run Two-Key Defense Regression
    try:
        run_two_key_tests()
    except Exception as e:
        print(f"\n[ERROR] Two-Key Defense Test failed: {e}")
        return 1

    # 3. Run Master Project Integrity Suite (61 tests)
    rc_master = run_master_tests()
    return rc_master


if __name__ == "__main__":
    sys.exit(main())
