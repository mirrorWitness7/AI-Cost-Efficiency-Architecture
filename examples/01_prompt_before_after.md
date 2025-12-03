# Example 1 – Prompt Before / After

## Task
Summarize a 10‑page internal policy and propose 3 action items.

### ❌ Before (high entropy)

> "Can you read this whole policy and tell me what you think?  
> I need some ideas to improve things, just brainstorm freely."

Problems:
- no target length
- no audience
- "brainstorm" → invites scatter

### ✅ After (lower entropy)

> You are an internal policy analyst.  
> Goal: help a busy manager understand the **practical impact** of this policy.  
> 
> 1. Read the attached policy.  
> 2. Produce:
>    - a 200‑word summary
>    - exactly 3 action items for the operations team
> 3. Avoid legal jargon. Write in plain English.

Result:
- fewer tokens
- 1–2 refinement turns instead of 5–6
- operator reports less fatigue
