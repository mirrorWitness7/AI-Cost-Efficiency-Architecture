# AI Lab Integration

For teams running many prompts / agents per day, integrate this repo as:

1. **An internal spec**
   - Add the efficiency equation and entropy rules to your internal wiki.
   - Make "entropy score" part of incident reviews (alongside latency, cost).

2. **A lightweight tracker**
   - Start with a simple spreadsheet populated from `data/sample_sessions.csv`.
   - Once it works, wire it into your logging pipeline.

3. **A review ritual**
   - Weekly: look at 5 highest‑entropy sessions.
   - Ask: what pattern caused the scatter? vague prompts, wrong tools, etc.
   - Patch the **process**, not just the prompt.

The tools in `tools/` are deliberately small and dependency‑free so they can
be embedded anywhere (Jupyter, backend scripts, internal dashboards).
