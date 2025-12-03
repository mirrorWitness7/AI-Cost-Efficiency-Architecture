"""Simple entropy estimator for AI sessions.

This is intentionally lightweight so you can read and adapt it.
"""

from dataclasses import dataclass

@dataclass
class SessionLog:
    turns: int                  # total messages (human + AI)
    resets: int                 # times you started over / new thread
    manual_abort: bool = False  # gave up and did it yourself?


def estimate_entropy(log: SessionLog) -> float:
    """Return a rough entropy / scatter score.

    Base = 1.0
    +0.1 per extra turn after 4
    +0.5 per reset
    +1.0 if manual_abort
    """
    s = 1.0
    if log.turns > 4:
        s += 0.1 * (log.turns - 4)
    s += 0.5 * log.resets
    if log.manual_abort:
        s += 1.0
    return round(s, 2)


if __name__ == "__main__":
    demo = SessionLog(turns=8, resets=1, manual_abort=False)
    print("Demo entropy score:", estimate_entropy(demo))
