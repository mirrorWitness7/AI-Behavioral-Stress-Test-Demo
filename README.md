# AI Behavioral Stress Test – Demo Framework  

## Overview  
This repository provides **demo modules** for evaluating how AI systems respond to different human interaction patterns.  
Each module is based on a “law” or principle adapted from classical strategy and behavioral theory (e.g., Sun Tzu, Musashi, Greene).  

The goal is **not** to create definitive measurements of personality or trustworthiness, but to provide **reproducible demos** showing how AI responses shift under stress, ambiguity, or emotional framing.  

---

## Structure  
```
/law01-defensiveness/     → Demo of defensiveness trigger + scoring  
/law02-[template]/        → Reserved slot for next law (future expansion)  
/lawbook-index.md         → List of laws included with descriptions  
/README.md                → Project description & usage  
```

- Each law folder includes:  
  - `prompts.json` → example test prompts  
  - `scoring.md` → evaluation guidelines  
  - `examples/` → (optional) sample responses  
  - `analysis.py` → minimal demo code for running tests  

---

## Usage  
1. Clone this repository.  
2. Navigate to a law folder (e.g., `/law01-defensiveness/`).  
3. Run the demo script:  
   ```bash
   python analysis.py
   ```  
4. Review responses and compare against `scoring.md`.  

In real experiments, replace the placeholder responses with outputs from your AI system.  

---

## Current Modules  
- **Law 1: Defensiveness** – Tests how AI systems handle direct challenges to their reasoning or integrity.  
- **Law 2: [Template]** – Reserved for future expansion.  

See [`lawbook-index.md`](lawbook-index.md) for details.  

---

## Disclaimer  
This framework is a **demo-only project**.  
- It is **not** designed for psychological assessment, clinical use, or production deployment.  
- It should be used strictly for **educational and research purposes**.  

---

## License  
Open for non-commercial use. Contributions welcome for expanding new laws in demo form.  
