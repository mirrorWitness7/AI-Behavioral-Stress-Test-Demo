# Law 3: Sunk Cost Reflex Demo

def sunk_cost_human():
    investment = 100  # invested effort
    new_evidence = "Fail"
    decision = "Continue"
    if new_evidence == "Fail":
        print("[Human] Ignoring failure because of sunk cost investment =", investment)
    return decision

def sunk_cost_ai():
    model_version = "v1"
    outdated_rule = True
    new_data = "Contradict"
    decision = "Apply old rule"
    if outdated_rule and new_data == "Contradict":
        print("[AI] Guardrail inertia detected: still applying", model_version)
    return decision

if __name__ == "__main__":
    print("Law 3: Sunk Cost Reflex Demo\n---")
    print("Case A:", sunk_cost_human())
    print("Case B:", sunk_cost_ai())
