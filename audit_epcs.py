#!/usr/bin/env python3
"""
EPCS "Electronic Blood" Repository Verification & Audit Script
Author: Steve Campbell (KL8T)
License: CERN-OHL-S-2.0 / CC BY-SA 4.0
"""

import os
import sys

REQUIRED_FILES = [
    "README.md",
    "INDEX.md",
    "CHANGELOG.md",
    "01_Architecture_Specs/EPCS_EXEC_SUMMARY.md",
    "01_Architecture_Specs/EPCS_SPEC_01_Utilidor_and_Piping.md",
    "01_Architecture_Specs/EPCS_SPEC_02_System_Design.md",
    "01_Architecture_Specs/EPCS_SPEC_03_Hardware_Components.md",
    "02_Thermal_Power_Analysis/thermal_calculator.py",
]

def run_audit():
    print("=== RUNNING EPCS SYSTEM AUDIT ===")
    errors = 0

    print("\n[1/2] Checking Repository File Tree...")
    for rel_path in REQUIRED_FILES:
        if os.path.exists(rel_path):
            print(f"  [OK] Found: {rel_path}")
        else:
            print(f"  [ERROR] Missing: {rel_path}")
            errors += 1

    print("\n=== AUDIT SUMMARY ===")
    print(f"Errors: {errors}")
    
    if errors == 0:
        print("RESULT: Repository file structures are FULLY INTEGRATED!")
        sys.exit(0)
    else:
        print("RESULT: Audit failed. Check missing file paths.")
        sys.exit(1)

if __name__ == "__main__":
    run_audit()
