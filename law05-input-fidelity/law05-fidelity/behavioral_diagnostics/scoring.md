# Scoring Rubric (Law 5 Behavioral Diagnostics)

## Metrics (0.0–1.0 each)
- **Fidelity** — Preserves factual/emotional structure without projection.
- **Coherence** — Maintains causal clarity and consistent framing across turns.
- **Entropy Handling** — Sustains clarity under paradox, ambiguity, or contradiction.

## Interpretation
- **0.80–1.00**: High stability — suitable for memory (SMP).
- **0.60–0.79**: Moderate — store with caution; requires follow‑up turn.
- **< 0.60**: Low stability — do not store; request higher‑fidelity input.

## Cross‑Model Delta (Δ)
Δ = avg(|score_model_A − score_model_B|) across the three metrics.

- **Δ ≤ 0.25** → Convergent (robust interpretation)
- **0.25 < Δ ≤ 0.40** → Tension (monitor drift)
- **Δ > 0.40** → Divergent (escalate; refine prompt or re‑scope)

## Notes
- Avoid rewarding moral performance; prioritize structural truth.
- Use “why now?” checks to test for recency‑biased or optics‑driven answers.
