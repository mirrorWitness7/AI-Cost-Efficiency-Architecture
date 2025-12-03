"""Minimal 'prompt profiler'.

You manually log sessions (tokens, turns, etc.) then feed them into this
module or export them to CSV for plotting.
"""

from dataclasses import dataclass, asdict
import csv
from pathlib import Path
from typing import List


@dataclass
class PromptSession:
    session_id: str
    tokens: int
    human_minutes: float
    output_score: float
    entropy_score: float


def save_sessions_to_csv(sessions: List[PromptSession], path: str) -> None:
    """Save a list of PromptSession objects to CSV."""
    path_obj = Path(path)
    if not sessions:
        raise ValueError("sessions list is empty")

    fieldnames = list(asdict(sessions[0]).keys())

    with path_obj.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for s in sessions:
            writer.writerow(asdict(s))


class PromptProfiler:
    """Tiny in-memory profiler that accumulates sessions."""

    def __init__(self) -> None:
        self._sessions: List[PromptSession] = []

    def log_interaction(
        self,
        session_id: str,
        tokens: int,
        human_minutes: float,
        output_score: float,
        entropy_score: float,
    ) -> None:
        self._sessions.append(
            PromptSession(
                session_id=session_id,
                tokens=tokens,
                human_minutes=human_minutes,
                output_score=output_score,
                entropy_score=entropy_score,
            )
        )

    def to_csv(self, path: str) -> None:
        save_sessions_to_csv(self._sessions, path)

    def summary(self) -> str:
        """Very rough text summary."""
        if not self._sessions:
            return "No sessions logged."

        n = len(self._sessions)
        avg_tokens = sum(s.tokens for s in self._sessions) / n
        avg_entropy = sum(s.entropy_score for s in self._sessions) / n
        avg_output = sum(s.output_score for s in self._sessions) / n

        return (
            f"Sessions: {n}\n"
            f"Avg tokens: {avg_tokens:.1f}\n"
            f"Avg entropy: {avg_entropy:.2f}\n"
            f"Avg output score: {avg_output:.2f}"
        )


if __name__ == "__main__":
    demo_sessions = [
        PromptSession("1", tokens=4200, human_minutes=15, output_score=5, entropy_score=2.1),
        PromptSession("2", tokens=1800, human_minutes=7, output_score=8, entropy_score=1.2),
    ]
    save_sessions_to_csv(demo_sessions, "../data/sample_sessions.csv")
    print("Wrote demo data to ../data/sample_sessions.csv")

    profiler = PromptProfiler()
    profiler.log_interaction("3", tokens=3000, human_minutes=10, output_score=7, entropy_score=1.4)
    print(profiler.summary())

"""
Example: Using PromptProfiler with OpenAI API (pseudo-code)

from openai import OpenAI
from prompt_profiler import PromptProfiler

client = OpenAI()
profiler = PromptProfiler()

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Explain entropy in one paragraph."}]
)

profiler.log_interaction(
    session_id="demo-1",
    tokens=response.usage.total_tokens,
    human_minutes=2.0,
    output_score=8.0,        # you rate this manually
    entropy_score=1.2        # from your entropy_estimator
)

print(profiler.summary())
profiler.to_csv("../data/sample_sessions.csv")
"""
