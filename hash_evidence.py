"""Calculate SHA-256 for project evidence files and write a manifest."""
from pathlib import Path
import hashlib, csv
ROOT = Path(__file__).resolve().parents[1]
TARGETS = [
    ROOT / "03_Evidence/source_media/omega_synthetic_evidence_fixture.zip",
    ROOT / "04_Malware/ransomware_simulator.py",
    ROOT / "05_Logs/sample_logs/master_events.csv",
]
OUT = ROOT / "03_Evidence/hash_manifest.csv"
rows = []
for path in TARGETS:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    rows.append([path.relative_to(ROOT).as_posix(), path.stat().st_size, "SHA-256", h.hexdigest()])
with OUT.open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["relative_path","size_bytes","algorithm","sha256"])
    w.writerows(rows)
print(f"Wrote {len(rows)} hashes to {OUT}")
for row in rows:
    print(row[0], row[3])
