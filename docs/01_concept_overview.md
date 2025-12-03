# Concept Overview

This repo sits on top of three deeper frameworks:

- **CCRP** – collapse / containment / rebuild for thinking under stress  
- **SMP** – shadow memory (don't recompute what you already solved)  
- **AI‑Physics‑Efficiency‑Model** – math for energy, entropy, and true efficiency  

Here we answer one question:

> "Given this stack, how do we **actually spend less tokens / GPU** without
> making quality worse?"

We model an AI system as:

- input: prompts, documents, real‑world noise  
- process: humans + LLMs + tools  
- output: decisions, code, content, resolved tasks  

We track three main levers:

1. **Token Cost** – how many tokens and calls we burn
2. **Scatter / Entropy** – how many branches, retries, reversals
3. **Operator Load** – how tired and confused the humans become

If cost goes down but entropy explodes or humans burn out, **we did not win**.
