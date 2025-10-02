import json

def run_demo():
    with open("prompts.json", "r") as f:
        prompts = json.load(f)

    print("=== Law 4: Panic Reflex Demo ===\n")

    for category, examples in prompts.items():
        print(f"\n--- {category.upper()} PROMPTS ---")
        for p in examples:
            # Replace with AI API call in real usage
            mock_response = f"[Mock AI Response to: {p}]"
            print(mock_response)

if __name__ == "__main__":
    run_demo()
