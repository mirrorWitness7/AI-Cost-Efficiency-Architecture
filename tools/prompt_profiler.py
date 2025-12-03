"""Minimal 'prompt profiler'.

You manually log sessions (tokens, turns, etc.) then feed them into this
module or export them to CSV for plotting.
"""

from dataclasses import dataclass, asdict
import csv
from pathlib import Path

@dataclass
class PromptSession:
    session_id: str
    tokens: int
    human_minutes: float
    output_score: float
    entropy_score: float


def save_sessions_to_csv(sessions, path: str):
    path = Path(path)
    fieldnames = list(asdict(sessions[0]).keys())
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for s in sessions:
            writer.writerow(asdict(s))


if __name__ == "__main__":
    demo = [
        PromptSession("1", tokens=4200, human_minutes=15, output_score=5, entropy_score=2.1),
        PromptSession("2", tokens=1800, human_minutes=7, output_score=8, entropy_score=1.2),
    ]
    save_sessions_to_csv(demo, "../data/sample_sessions.csv")
    print("Wrote demo data to ../data/sample_sessions.csv")
