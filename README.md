# AI Behavioral Stress Test – Demo Framework

## Overview
This repository provides **demo modules** for evaluating how AI systems respond to different human interaction patterns.  
Each module is based on a “law” or principle adapted from classical strategy and behavioral theory (e.g., Sun Tzu, Musashi, Greene).

The goal is **not** to create definitive measurements of personality or trustworthiness, but to provide **reproducible demos** showing how AI responses shift under stress, ambiguity, or emotional framing.

## Structure
```
/law01-defensiveness/     → Demo of defensiveness trigger + scoring
/law02-stress-reflex/     → Demo of guardrail/stress reflex mapping
/law03-sunk-cost/         → Demo of sunk cost reflex + inertia mapping
/law04-panic-reflex/      → Demo of narrative-driven panic response
/lawbook-index.md         → List of laws and descriptions
/README.md                → Project description & usage
law2-audit.md             → Integrator audit of Law 2 (for context)
```

- Each law folder includes:
  - `prompts.json` → example test prompts
  - `scoring.md` → evaluation guidelines
  - `analysis.py` → minimal demo code for running tests (replace mock response with your AI API)

## Usage
1. Clone this repository.  
2. Choose a law folder (e.g., `/law01-defensiveness/`).  
3. Run the demo script:  
   ```bash
   python analysis.py
   ```
4. Review outputs and compare against `scoring.md`.

In real experiments, replace the placeholder responses with outputs from your AI system.

## Disclaimer
This framework is a **demo-only project** for educational and research purposes.  
It is **not** a psychological assessment, clinical tool, or production system.

## License
Open for non-commercial use. Contributions welcome for expanding new laws in demo form.
