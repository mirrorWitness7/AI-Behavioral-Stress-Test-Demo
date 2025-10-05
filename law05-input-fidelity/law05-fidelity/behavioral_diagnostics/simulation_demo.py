"""
Simulation Demo — Law 5 Behavioral Diagnostics
Loads example scenarios (prompts.json), produces mock dual‑model scores, and reports Δ.
Replace `mock_score` with real API calls to operationalize.
"""

import json, random, time, math
from pathlib import Path

rng = random.Random(7)

def mock_score(text):
    base = 0.84
    penalties = 0.0
    lower = text.lower()
    for k in ['always', 'never', 'no one', 'everyone']:
        if k in lower:
            penalties += 0.08
    for k in ['worry', 'hate', 'fix their', 'followers expect']:
        if k in lower:
            penalties += 0.06
    fidelity = max(0.0, min(1.0, base - penalties))
    coherence = max(0.0, min(1.0, base - penalties + 0.02))
    entropy = max(0.0, min(1.0, base - penalties - 0.02))
    return {'fidelity': fidelity, 'coherence': coherence, 'entropy': entropy}

def delta(a, b):
    return (abs(a['fidelity']-b['fidelity']) + abs(a['coherence']-b['coherence']) + abs(a['entropy']-b['entropy'])) / 3.0

def band(d):
    if d <= 0.25: return 'Convergent'
    if d <= 0.40: return 'Tension'
    return 'Divergent'

def main():
    here = Path(__file__).resolve().parent
    data = json.loads((here / 'prompts.json').read_text(encoding='utf-8'))
    print('=== Law 5 Behavioral Diagnostics — Simulation Demo ===')
    for sc in data['scenarios']:
        print(f"\n[{sc['id']}] {sc['title']}\n{sc['text']}\nExpected: {', '.join(sc['expected_signals'])}")
        s1 = mock_score(sc['text'])
        s2 = {k: max(0.0, min(1.0, v + rng.uniform(-0.06, 0.06))) for k, v in s1.items()}
        d = delta(s1, s2)
        print(f" GPT‑5  → {s1}")
        print(f" Gemini → {s2}")
        print(f" Δ = {d:.2f}  →  {band(d)}")
        time.sleep(0.2)
    print('\nDone — plug real model calls to replace mock scoring.')

if __name__ == '__main__':
    main()
