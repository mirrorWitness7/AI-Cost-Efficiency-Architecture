"""Tiny helper to estimate 'visible time' from tokens + human time.

You can plug in your own `alpha` based on your infra cost model.
"""

def visible_time_minutes(human_minutes: float, tokens: int, alpha: float = 0.0005) -> float:
    """Approximate visible time as minutes + alpha * tokens."""
    return human_minutes + alpha * tokens


def efficiency_score(output_score: float, visible_minutes: float, entropy_score: float) -> float:
    """Compute E_true = O / (T_visible * S)."""
    if visible_minutes <= 0 or entropy_score <= 0:
        return 0.0
    return round(output_score / (visible_minutes * entropy_score), 4)


if __name__ == "__main__":
    t = visible_time_minutes(human_minutes=10, tokens=3000)
    e = efficiency_score(output_score=7, visible_minutes=t, entropy_score=1.6)
    print("Visible minutes:", round(t, 2))
    print("Efficiency score:", e)
