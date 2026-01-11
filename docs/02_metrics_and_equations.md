# Metrics & Equations

We keep the math intentionally simple so it survives contact with  
non-math stakeholders, finance teams, and auditors.

Everything here is designed to be:
- explainable
- computable from logs
- consistent if rules remain fixed
- difficult to game silently

---

## Core Efficiency

E_true = O / (T_visible * S_total)

Where:

O = output quality score (0–10, defined per team)  
T_visible = visible effort (human minutes + token cost proxy)  
S_total = entropy multiplier (1.0 = clean workflow, higher = messy / inefficient)

Interpretation:
- High output alone does NOT mean efficiency  
- Low cost alone does NOT mean efficiency  
- Confusion and rework multiply cost non-linearly  

---

## Output (O): Human-Graded Score

O is scored per session using a simple rubric.

0–2: unusable, wasted  
3–5: partial, heavy rework needed  
6–8: usable with light edits  
9–10: copy-paste quality, high confidence  

Important:
- If the same person produces the work and grades O, this measures perceived usefulness, not external correctness.
- For audit-grade use, O should be graded by someone independent of the operator.

---

## Visible Effort (T_visible)

T_visible is estimated as:

T_visible = human_minutes + (alpha * tokens)

Where:
- human_minutes = time the operator spent prompting, thinking, editing
- tokens = total input + output tokens for the session
- alpha = conversion factor from tokens to equivalent minutes

Example alpha:
- alpha = 0.0005 minutes per token

The absolute value of alpha does not matter as long as it is used consistently across all sessions.

---

## Entropy (S): Rule-Based Penalty Multiplier

Entropy is not a vibe.  
It is a penalty multiplier derived from observable workflow behavior.

Base:
- Every session starts with S_base = 1.0

Add penalties based on log-detectable events:

+0.2 for each extra turn beyond the first 3 turns on the same task  
+0.5 for each explicit reset ("start over", "new approach", "forget previous")  
+1.0 if the human abandons AI and completes the task manually  

These signals can be detected from:
- chat logs
- UI events (new chat, restart, abort)
- keywords ("again", "no that's wrong", "forget it", etc.)
- session metadata

No LLM is required to compute these penalties.

---

## Zombie Thread Penalty (Long-Context Drift)

A zombie thread is when:
- the conversation context becomes very long
- most of that history is no longer relevant
- the user keeps patching instead of restarting cleanly

We penalize this because it inflates cost while degrading clarity.

Definitions:

L_ctx = total tokens currently in the conversation  
L_max = maximum healthy context length (team-defined, e.g. 4000 tokens)  

Length penalty rule:

If L_ctx <= L_max:
  length_penalty = 0

If L_ctx > L_max:
  length_penalty = ((L_ctx - L_max) / L_max) * lambda_len

Where:
- lambda_len is a weight such as 0.3–0.5 depending on how aggressive you want the penalty

Example:
- L_ctx = 8000  
- L_max = 4000  
- lambda_len = 0.4  

length_penalty = ((8000 - 4000) / 4000) * 0.4  
length_penalty = 1 * 0.4  
length_penalty = +0.4 added to entropy

Optional zombie flag (stricter mode):

If:
- L_ctx is far above L_max (e.g. >2x), AND
- the user continues without restructuring the task,

then apply an additional fixed penalty:

zombie_flag_penalty = +0.8 to +1.0

This is intentionally conservative and can be disabled in strict audit mode.

---

## Final Entropy

S_total = S_base + length_penalty + zombie_flag_penalty

Where:
- S_base = penalties from retries, resets, manual aborts
- length_penalty = penalty for oversized context
- zombie_flag_penalty = optional extra penalty for extreme long-context misuse

---

## Why This Design Works

This entropy model:

- Is mostly deterministic  
- Can be computed from logs  
- Does not rely on trusting an LLM’s honesty  
- Encourages shorter, cleaner, more structured workflows  
- Penalizes hidden inefficiency without moral judgment  

It does not attempt to model human psychology.  
It models observable operational behavior.

---

## Explicit Limitation

This framework measures structural efficiency, not truth.

A workflow can be:
- efficient  
- fast  
- low entropy  

and still produce:
- incorrect conclusions  
- biased outputs  
- strategically misleading reports  

This is intentional and documented.

---

## Core Principle

If efficiency cannot be calculated because required variables are missing,  
the correct result is **refusal to compute**, not a guess.

Undefined metrics are treated as a diagnostic signal:
- unclear success criteria  
- invisible human effort  
- untracked rework  
- missing instrumentation  

The framework does not fix that.  
It exposes it.
