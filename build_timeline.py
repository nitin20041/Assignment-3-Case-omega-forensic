"""Build a normalized incident timeline from the synthetic CSV event logs."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "05_Logs" / "sample_logs"
OUTPUT = ROOT / "05_Logs" / "results"
OUTPUT.mkdir(parents=True, exist_ok=True)

frames = []
for path in sorted(INPUT.glob("*.csv")):
    df = pd.read_csv(path)
    if not df.empty:
        frames.append(df)
if not frames:
    raise SystemExit("No CSV logs found.")

events = pd.concat(frames, ignore_index=True).drop_duplicates()
events["timestamp_parsed"] = pd.to_datetime(events["timestamp"], utc=True, errors="coerce")
events = events.dropna(subset=["timestamp_parsed"]).sort_values("timestamp_parsed")
events.to_csv(OUTPUT / "attack_timeline.csv", index=False)

# Plot event positions in IST; the data is synthetic and labelled accordingly.
plot = events.copy()
plot["time_ist"] = plot["timestamp_parsed"].dt.tz_convert("Asia/Kolkata")
fig, ax = plt.subplots(figsize=(12, 6))
y = list(range(len(plot)))
ax.scatter(plot["time_ist"], y)
for i, (_, row) in enumerate(plot.iterrows()):
    ax.annotate(f'{row["source"]}: {row["event_description"][:42]}',
                (row["time_ist"], i), xytext=(6, 2), textcoords="offset points", fontsize=7)
ax.set_yticks([])
ax.set_title("Case Omega – Synthetic Event Timeline (IST)")
ax.set_xlabel("Time (IST)")
ax.grid(axis="x", alpha=.3)
fig.tight_layout()
fig.savefig(OUTPUT / "attack_timeline.png", dpi=180)
print(f"Events correlated: {len(events)}")
print(f"Timeline: {OUTPUT / 'attack_timeline.csv'}")
print(f"Visualization: {OUTPUT / 'attack_timeline.png'}")
