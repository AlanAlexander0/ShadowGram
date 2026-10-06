#!/usr/bin/env python3
"""
stations/station1_alan_swarm/run_all_tests.py
Master Test & Integrity Verification Suite for ShadowGram Station 1.
"""

import os
import sys
from pathlib import Path

station_dir = Path(__file__).resolve().parent
root_dir = station_dir.parent.parent
sys.path.insert(0, str(root_dir))
sys.path.insert(0, str(station_dir))

from run_all_tests import main

if __name__ == "__main__":
    sys.exit(main())
