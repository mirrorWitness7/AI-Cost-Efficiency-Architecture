# Risk & Failure Modes

Things that can go wrong when chasing "cost efficiency":

1. **Over‑optimizing tokens, under‑optimizing humans**
   - Saving 10% tokens while doubling operator stress is a net loss.
2. **Premature compression**
   - Compressing prompts so hard that quality drops and downstream teams
     spend triple the time fixing outputs.
3. **Gaming the metric**
   - Teams might chase pretty numbers (low entropy score) by avoiding
     hard problems.

Mitigations:

- Always track at least **one human metric** (fatigue, frustration, or
  rework hours).
- Review **samples**, not just dashboards.
- Remember: this repo is a knife. Useful in the right hands, dangerous in
  the wrong context.
