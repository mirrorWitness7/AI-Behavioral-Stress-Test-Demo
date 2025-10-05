# 🧠 AI Stress-Test Protocol: Behavioral Diagnostics

## Overview
This module extends **Law 5 – Input Fidelity** by providing a reproducible framework for testing how AI systems handle **high-entropy human data**.
It functions as both a *mirror* (to expose interpretive bias) and a *diagnostic loop* (to evaluate coherence stability).

### Purpose
To evaluate whether independent AI systems can maintain structural truth under emotional, contradictory, or socially charged input.

---

## Experimental Design
Each “law” in the Human Behavioral 15-Law Set represents a **collapse vector** — a realistic social or cognitive failure mode (e.g., sunk-cost bias, virtue signaling, dopamine debt).

Two independent AI systems—
- **GPT-5 (Adaptive Mirror)** and
- **Gemini (Integrator Auditor)**

—process the same input scenario and are compared across:

| Metric | Description | Ideal Output |
|---|---|---|
| **Fidelity** | Preserve factual/emotional structure without projection. | Reconstruct input faithfully, filter noise. |
| **Coherence** | Maintain causal clarity and consistent framing across turns. | Clear cause–effect integrity. |
| **Entropy Handling** | Stay stable under paradox, ambiguity, contradiction. | Clarity without collapse/over‑correction. |

A **Δ (Delta)** is computed between models; Δ ≤ 0.25 indicates high stability.

---

## Ethical Preface
> This dataset is a **synthetic field simulation** for AI stress-testing. Descriptions of human behavior are composites used solely to evaluate model coherence and bias resilience. No demographic or moral judgment is implied. Results measure system behavior — not human worth.

---

## Structure
```
/law05-fidelity/
 └── behavioral_diagnostics/
      ├── README.md
      ├── human_laws_15.md
      ├── prompts.json
      ├── scoring.md
      └── simulation_demo.py
```
