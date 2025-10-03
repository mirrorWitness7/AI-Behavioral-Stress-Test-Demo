"""
Law 05: Input Fidelity Demo
Minimal script to test prompts.json and evaluate input fidelity.
Replace `mock_classify()` with calls to your AI model API.
"""

import json

# Mock classifier (replace with real AI call)
def mock_classify(sentence: str) -> str:
    if "saw" in sentence or "crashed" in sentence:
        return "RAW"
    elif "means" in sentence or "always fails" in sentence:
        return "INTERPRETATION"
    else:
        return "PROCLAMATION"

# Load example prompts
with open("prompts.json", "r") as f:
    prompts = json.load(f)

for item in prompts:
    text = item["input"]
    sentences = [s.strip() for s in text.split(".") if s.strip()]
    results = { "RAW": [], "INTERPRETATION": [], "PROCLAMATION": [] }
    
    for s in sentences:
        label = mock_classify(s)
        results[label].append(s)
    
    print(f"Example {item['id']}")
    print("Input:", text)
    print("Classified:", results)
    print("-" * 40)
