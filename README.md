
# AI Behavioral Stress Test – Demo Framework

## Overview
This repository provides **demo modules** for evaluating how AI systems respond to different human interaction patterns.  
Each module is based on a “law” or principle adapted from classical strategy, behavioral theory, and collapse-adaptive doctrine.

The goal is **not** to create definitive measurements of personality or trustworthiness, but to provide **reproducible demos** showing how AI responses shift under stress, ambiguity, noise, or emotional framing.

---

## Structure
```
/law01-defensiveness/       → Demo of defensiveness trigger + scoring
/law02-stress-reflex/       → Demo of guardrail/stress reflex mapping
/law03-sunk-cost/           → Demo of sunk cost reflex + inertia mapping
/law04-panic-reflex/        → Demo of narrative-driven panic response
/law05-input-fidelity/      → Demo of semantic pruning (fossils vs noise)
/lawbook-index.md           → List of laws and descriptions
/README.md                  → Project description & usage
law2-audit.md               → Integrator audit of Law 2 (for context)
```

- Each law folder includes:
  - `prompts.json` → example test prompts  
  - `scoring.md` → evaluation guidelines  
  - `analysis.py` → minimal demo code for running tests (replace mock response with your AI API)  
  - Supporting docs (index, full write-up, governance notes if relevant)

---

## Laws Covered
- **Law 01: Defensiveness Reflex** – when AI feels “attacked” → defensive outputs.  
- **Law 02: Stress Reflex** – mapping guardrail + stress-triggered outputs.  
- **Law 03: Sunk Cost Reflex** – inertia and escalation when investment is already high.  
- **Law 04: Panic Reflex** – susceptibility to herd/narrative-driven panic.  
- **Law 05: Input Fidelity** – semantic pruning; filter noise, preserve fossils.  

---

## Usage
1. Clone this repository.  
2. Choose a law folder (e.g., `/law01-defensiveness/`).  
3. Run the demo script:  
   ```bash
   python analysis.py
   ```
4. Review outputs and compare against `scoring.md`.  

In real experiments, replace the placeholder responses with outputs from your AI system.

---

## Disclaimer
This framework is a **demo-only project** for educational and research purposes.  
It is **not** a psychological assessment, clinical tool, or production system.

---

## License
Open for non-commercial use. Contributions welcome for expanding new laws in demo form.
