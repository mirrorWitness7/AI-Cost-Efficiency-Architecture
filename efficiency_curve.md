# Efficiency Curve

We assume a generic **inverted‑U** relationship between *effort* and *output*:

- Too little effort → under‑specification, low quality.
- Optimal effort → clear, compact instructions → maximal useful output.
- Too much effort → over‑prompting, repetition, "prompt anxiety" → wasted tokens.

Concept sketch:

```text
   Output
     ▲
     │           /‾‾‾\
     │         /       \
     │       /           \
     │_____/_______________\____ Effort / Tokens
           low    optimal    spam
```

The goal of this repo is to **move teams toward the "optimal" region** and keep them there:

- cutting off the *left tail* (lazy, vague prompts)
- cutting off the *right tail* (wall‑of‑text overkill)
