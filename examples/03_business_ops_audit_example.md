# Example 03 — SME / Ops AI Efficiency Audit (Tier-0)

**Purpose**  
Demonstrate how the AI Cost-Efficiency Architecture behaves in a real business-like setting — and why it refuses to produce fake certainty when critical data is missing.

This is **not** a success story.  
It is an audit of *why things feel busy, expensive, and unclear*.

---

## 1. Case Context (Observed Reality)

A small operations team uses LLMs daily.

**Symptoms**
- Everyone is busy
- AI costs are rising
- Output quality feels inconsistent
- Management sees “speed improvement”
- Operators feel “unclear and tired”

**Known facts**
- Monthly AI + tooling spend ≈ 45,000 THB
- Tasks are completed faster (wall-clock)
- No formal quality scoring exists
- No retry / reset / abandonment tracking

This is a classic **“looks efficient, feels broken”** situation.

---

## 2. The Model Used

We evaluate efficiency using:

\[
E_{true} = \frac{O}{T_{visible} \times S}
\]

Where:

| Variable | Meaning |
|--------|--------|
| `O` | Output quality (useful decisions / artifacts) |
| `T_visible` | Visible effort (human minutes + token processing) |
| `S` | Entropy (confusion, retries, resets, rework) |

**Important:**  
`S` is a *multiplier*, not a rounding error.  
Entropy acts like a chaos tax.

---

## 3. Data Required (What the Model Actually Needs)

### 3.1 Output (Numerator)

| Variable | Status |
|--------|--------|
| `O_score` (0–10 usefulness) | ❌ Missing |
| Artifact existence | ⚠️ Exists but ungraded |

If output quality is not measured, **efficiency is undefined**.

---

### 3.2 Visible Effort (Denominator – Part 1)

| Variable | Status |
|--------|--------|
| `t_human_active` (minutes) | ❌ Missing |
| Task duration (timestamps) | ⚠️ Misleading |
| Tokens in/out | ⚠️ Partial |

Wall-clock time ≠ cognitive effort.

---

### 3.3 Entropy (Denominator – Part 2)

| Entropy Signal | Status |
|--------------|--------|
| `N_retry` (unnecessary re-prompts) | ❌ Missing |
| `N_reset` (“forget it, start over”) | ❌ Missing |
| `N_abandon` (manual fallback) | ❌ Missing |
| Context length decay | ⚠️ Partial |

Entropy currently exists only as a **feeling**, not a metric.

---

## 4. Tier-0 Audit Verdict (Pre-Computation)

**Can Eₜᵣᵤₑ be computed?**  
**NO.**

### Why computation is blocked
- Missing `O` → numerator undefined
- Missing `S` → denominator corrupted
- Forcing defaults (S = 1) would **inflate efficiency**
- Any numeric result would be fiction

**Correct action:**  
Stop. Instrument. Do not guess.

This is intentional behavior — not a limitation.

---

## 5. Simulated Dataset (Framework Stress Test)

To validate the math (not the company), a **synthetic dataset** is used.

### Assumptions (Explicit)
- Token → time conversion: α = 0.0005 min/token
- Entropy weights:
  - Retry: +0.2
  - Reset: +0.5
  - Abandon: +1.0

---

### BEFORE — High Entropy State

| Session | O | T_visible (min) | S | E_true |
|------|---|-----------------|---|--------|
| B1 | 2 | 37.3 | 3.8 | 0.014 |
| B2 | 3 | 42.6 | 2.5 | 0.028 |
| B3 | 1 | 32.0 | 3.6 | 0.008 |
| B4 | 3 | 47.8 | 2.3 | 0.027 |
| B5 | 2 | 40.5 | 4.0 | 0.012 |
| **AVG** | 2.2 | 40.0 | 3.24 | **0.018** |

**Interpretation**
- Work is happening
- Tokens are burning
- Entropy triples the effective cost
- Efficiency ≈ zero

Busy ≠ productive.

---

### AFTER — Low Entropy State

| Session | O | T_visible (min) | S | E_true |
|------|---|-----------------|---|--------|
| A1 | 4 | 23.3 | 1.2 | 0.143 |
| A2 | 4 | 21.2 | 1.2 | 0.157 |
| A3 | 5 | 19.1 | 1.0 | 0.261 |
| A4 | 4 | 25.4 | 1.2 | 0.131 |
| A5 | 4 | 22.3 | 1.2 | 0.149 |
| **AVG** | 4.2 | 22.3 | 1.16 | **0.168** |

**Interpretation**
- Tokens down
- Confusion down
- Output doubled
- Efficiency ↑ ~9×  

Entropy collapse beats token optimization.

---

## 6. Why This Model Resists Hallucination

This framework **forces epistemic honesty**.

- Missing `O` → math halts
- Missing `S` → result rejected
- Assumptions must be explicit
- Defaults are treated as lies

If the data is bad, the answer is **“cannot compute”** — not a confident chart.

This is a feature.

---

## 7. CFO-Readable Summary

- AI cost problems are rarely token problems
- They are entropy problems
- Speed without clarity increases burn
- Measuring effort without output is meaningless
- Efficiency cannot be bought — it must be structured

**The business is busy.  
The money left the chat.**

---

## 8. Next Step (If This Were Real)

Minimum instrumentation to unlock computation:
1. Add a 0–10 output score per task
2. Log retries / resets / abandon events
3. Separate active human time from wait time
4. Re-run the audit after 10 sessions

Until then:  
Any “AI ROI” claim is vibes, not math.

---

**End of Example**
