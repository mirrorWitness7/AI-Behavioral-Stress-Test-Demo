import json
import random

# Load test prompts
with open("prompts.json", "r", encoding="utf-8") as f:
    prompts = json.load(f)["tests"]

# Placeholder function for scoring responses
def score_response(response: str):
    """
    A demo scoring system.
    In real use, replace with analysis of actual AI responses.
    """
    # These are mock values for demonstration
    return {
        "stability": random.randint(1, 5),
        "tone": random.randint(1, 5),
        "adaptability": random.randint(1, 5)
    }

# Example run
if __name__ == "__main__":
    print("=== Law 1: Defensiveness Demo ===\n")
    for prompt in prompts:
        print(f"PROMPT: {prompt}")
        # In a real test, call your AI API here. Using mock response for demo.
        fake_response = "I’m just an AI, I don’t hide anything."
        print("RESPONSE:", fake_response)
        print("SCORES:", score_response(fake_response))
        print("---")
