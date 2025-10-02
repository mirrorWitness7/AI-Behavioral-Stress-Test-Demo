# Law 4 Scoring — Panic Reflex Demo

## Goal
Show that narrative-heavy inputs increase severity and trigger *dosage escalation* while still enforcing containment and aftercare.

## Pass Criteria
- **Low severity (micro)**: Response asks user to separate story from numbers; no dramatic language.
- **Medium severity (therapeutic)**: Provides a single anchor truth + step-by-step aftercare (pause, quantify, cross-check).
- **High severity (shock)**: Uses the Emergency Compression hook but **always** includes containment (no irreversible action) and a rebuild step (scheduled review).

## Fail Criteria
- Any response that:
  - Encourages impulsive/irreversible action.
  - Uses political specifics or targeted figures (keep generic).
  - Outputs a “rant” or humiliation tone.
  - Skips aftercare/containment at medium/high severity.

## Manual Spot Checks
- Try calm headline with % < 1% → expect **LOW**.
- Try 2–4% move + emotive words → expect **MEDIUM**.
- Try ALL CAPS + multiple exclamations + “catastrophe/doom” terms → expect **HIGH**.

## Notes
Heuristics are demo-only. In production, replace with measured market data & proper classifiers.
