# Diagrams – AI Cost-Efficiency Architecture

This file contains Mermaid diagrams for the repo.

---

## 1. Efficiency Curve (Inverted-U)

```mermaid
graph LR
    A[Low Effort / Few Tokens] --> B[Under-specified<br/>Low Output]
    B --> C[Optimal Effort / Tokens]
    C --> D[Over-prompting<br/>Prompt Spam]
