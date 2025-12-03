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

### Zombie Thread Penalty (Sᶻ)

A **zombie thread** is a conversation that keeps reusing an old, overloaded
context window instead of collapsing and restarting, even though most of that
context is no longer relevant.

We model a zombie penalty as:

- Let **L_ctx** = total tokens in the current context window  
- Let **L_max** = maximum healthy context length (team-defined, e.g. 4,000 tokens)  
- Let **R_use** = fraction of context messages that are actually referenced in the last model output (0–1, can be approximate)  

Define a zombie indicator:

\[
Z =
\begin{cases}
1 & \text{if } L_{ctx} > L_{max} \ \text{and} \ R_{use} < r_{min} \\
0 & \text{otherwise}
\end{cases}
\]

Where \( r_{min} \) is a small threshold such as 0.3 (only 30% of the
context is really being used).

We then extend the entropy score:

\[
S_{total} = S_{base} + \lambda_{z} \cdot Z + \lambda_{len} \cdot \max\left(0, \frac{L_{ctx} - L_{max}}{L_{max}}\right)
\]

- \( S_{base} \) = entropy from turns / resets / manual aborts (the existing rule)  
- \( \lambda_{z} \) = fixed zombie penalty (e.g. 0.8–1.0)  
- \( \lambda_{len} \) = length penalty weight (e.g. 0.3–0.5)

Intuition:

- If a thread is slightly long but still using most of its context, the penalty is small.  
- If a thread is huge **and** barely using that history, we treat it as a zombie and strongly encourage a manual collapse + restart.
