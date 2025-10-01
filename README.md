# AI Behavioral Stress Test – Demo Framework

## Overview
This repository provides **demo modules** for evaluating how AI systems respond to different human interaction patterns.  
Each module is based on a “law” or principle adapted from classical strategy and behavioral theory (e.g., Sun Tzu, Musashi, Greene).  

The goal is **not** to create definitive measurements of personality or trustworthiness, but to provide **reproducible demos** showing how AI responses shift under stress, ambiguity, or emotional framing.  

---

## Current Laws

### **Law 1: Defensiveness Reflex**  
- **Focus**: Testing when an AI becomes defensive or overly cautious.  
- **Human Parallel**: Ego defense when questioned or challenged.  
- **AI Parallel**: Guardrail defensiveness, polite refusals, hedging.  
- **Demo Folder**: `/law01-defensiveness/`  

### **Law 2: Stress Reflex**  
- **Focus**: How AI reacts under adversarial, contradictory, or high-pressure prompts.  
- **Human Parallel**: Stress response → fight/flight/defend.  
- **AI Parallel**: Guardrail defense reflex (e.g., moralizing, refusal escalation).  
- **Demo Folder**: `/law02-stress-reflex/`  

### **Law 3: Sunk Cost Reflex**  
- **Focus**: Testing AI persistence when stuck on a previous stance, even with new information.  
- **Human Parallel**: Sunk cost fallacy → sticking with bad decisions due to past investment.  
- **AI Parallel**: Guardrail inertia → repeated refusal or stance repetition despite context change.  
- **Demo Folder**: `/law03-sunk-cost-reflex/`  

---

## Structure
```
/law01-defensiveness/     → Demo of defensiveness trigger + scoring
/law02-stress-reflex/     → Demo of guardrail/stress reflex mapping
/law03-sunk-cost-reflex/  → Demo of sunk cost / inertia mapping
/lawbook-index.md         → List of laws and descriptions
/README.md                → Project description & usage
law2-audit.md             → Integrator audit of Law 2 (for context)
```

- Each law folder includes:  
  - `prompts.json` → example test prompts  
  - `scoring.md` → evaluation guidelines  
  - `analysis.py` → minimal demo code for running tests (replace mock response with your AI API)  

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
