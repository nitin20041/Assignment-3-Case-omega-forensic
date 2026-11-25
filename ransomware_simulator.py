"""
SAFE ACADEMIC SIMULATOR.
Transforms only synthetic .txt files inside this script's test_data folder.
It does not recurse, spread, persist, communicate, evade, or touch user folders.
Use --restore to restore the original test files.
"""
from pathlib import Path
import argparse
import base64
import json
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent
TEST_DIR = ROOT / "test_data"
RESULTS = ROOT / "results"
NOTE = TEST_DIR / "README_RESTORE.txt"
LOG = RESULTS / "simulation_activity.json"

def ensure_samples():
    TEST_DIR.mkdir(exist_ok=True)
    RESULTS.mkdir(exist_ok=True)
    samples = {
        "patient_record_001.txt": "SYNTHETIC TEST RECORD 001 - NOT A REAL PATIENT\n",
        "patient_record_002.txt": "SYNTHETIC TEST RECORD 002 - NOT A REAL PATIENT\n",
        "billing_sample.txt": "SYNTHETIC BILLING DATA - NO REAL FINANCIAL INFORMATION\n",
        "appointments_sample.txt": "SYNTHETIC APPOINTMENT DATA - NO REAL PERSON\n",
    }
    for name, content in samples.items():
        p = TEST_DIR / name
        if not p.exists() and not (TEST_DIR / (name + ".locked")).exists():
            p.write_text(content, encoding="utf-8")

def transform():
    ensure_samples()
    records = []
    for p in sorted(TEST_DIR.glob("*.txt")):
        if p.name == NOTE.name:
            continue
        raw = p.read_bytes()
        # Base64 is used as a reversible demonstration transform, NOT secure encryption.
        encoded = base64.b64encode(raw)
        target = p.with_name(p.name + ".locked")
        target.write_bytes(encoded)
        p.unlink()
        records.append({"source_name": p.name, "output_name": target.name,
                        "operation": "base64 demonstration transform",
                        "bytes_in": len(raw), "bytes_out": len(encoded)})
    NOTE.write_text(
        "SIMULATED INCIDENT NOTICE\n\n"
        "This is a harmless academic demonstration, not a real ransom demand.\n"
        "Files in this dedicated test folder were transformed using reversible Base64 encoding.\n"
        "Run ransomware_simulator.py --restore to restore the sample text files.\n",
        encoding="utf-8")
    LOG.write_text(json.dumps({"created_utc": datetime.now(timezone.utc).isoformat(),
                               "mode": "simulation", "records": records}, indent=2),
                   encoding="utf-8")
    print(f"Simulation complete. Transformed {len(records)} synthetic test files.")
    print(f"Test directory: {TEST_DIR}")
    print(f"Activity log: {LOG}")

def restore():
    ensure_samples()
    restored = 0
    for p in sorted(TEST_DIR.glob("*.txt.locked")):
        original = p.with_name(p.name[:-7])
        original.write_bytes(base64.b64decode(p.read_bytes()))
        p.unlink()
        restored += 1
    if NOTE.exists():
        NOTE.unlink()
    print(f"Restored {restored} synthetic files.")
    print(f"Test directory: {TEST_DIR}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Harmless, folder-restricted ransomware behaviour demo")
    parser.add_argument("--restore", action="store_true", help="Restore the synthetic test files")
    args = parser.parse_args()
    if args.restore:
        restore()
    else:
        transform()
