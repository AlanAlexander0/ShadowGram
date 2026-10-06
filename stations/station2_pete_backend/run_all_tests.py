#!/usr/bin/env python3
"""
stations/station2_pete_backend/run_all_tests.py
Master Test & Integrity Verification Suite for ShadowGram Station 2.
"""

import os
import sys
from pathlib import Path

# Add project root to sys.path so modules can be imported from root or station
station_dir = Path(__file__).resolve().parent
root_dir = station_dir.parent.parent
sys.path.insert(0, str(root_dir))
sys.path.insert(0, str(station_dir))

# Execute the master test runner
from run_all_tests import main

if __name__ == "__main__":
    sys.exit(main())
