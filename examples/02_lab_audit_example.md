# Example 2 – Mini Lab Audit

You can log a tiny sample of sessions like this:

| session_id | tokens | human_minutes | output_score | entropy_score |
|-----------:|-------:|--------------:|-------------:|--------------:|
| 1          |  4200  |      15       |      5       |      2.1      |
| 2          |  1800  |       7       |      8       |      1.2      |
| 3          |  9000  |      30       |      4       |      2.8      |

Then compute a **rough efficiency**:

\[
E_{true} = \frac{O}{T_{visible} \times S}
\]

You don’t need perfect precision. The point is to **compare before vs. after**
once you change prompts, tools, or operator training.
