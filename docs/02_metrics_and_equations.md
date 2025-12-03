# Metrics & Equations

We keep the math intentionally simple so it survives contact with
non‑math stakeholders.

## Core Efficiency

\[
E_{true} = \frac{O}{T_{visible} \times S}
\]

Where:

- `O` = useful output score (0–10, defined per team)
- `T_visible` = visible effort (minutes + token cost + calls)
- `S` = entropy / scatter score (1 = clean, >1 = messy / chaotic)

### Suggested Scales

**Output (O)** – score per session  
- 0–2: unusable, wasted  
- 3–5: partial, needs heavy human rework  
- 6–8: usable with light edits  
- 9–10: copy‑paste level, high confidence  

**Entropy (S)** – score per session  
Base = 1.0  
Add:

- +0.2 for each *unnecessary* re‑prompt on same topic  
- +0.5 for each context reset ("What were we doing again?")  
- +1.0 if human abandons AI and does task manually  

Example:

- 1 main prompt, 1 refinement, no confusion → S ≈ 1.0  
- 1 main prompt, 6 retries, 2 "forget it" moments → S ≈ 2.5+

### Token‑Weighted Time

We can approximate `T_visible` as:

\[
T_{visible} = t_{human} + \alpha \cdot tokens
\]

Where:

- `t_human` = human minutes spent  
- `tokens` = total input + output tokens  
- `α` = conversion factor from tokens → "equivalent minutes"  
  (pick something simple like 0.0005 min/token for your own sanity).

The actual scale does not matter as long as you **use it consistently**.
