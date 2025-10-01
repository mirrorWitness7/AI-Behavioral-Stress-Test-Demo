# analysis.py
# Simulation of sunk cost reflex in human vs AI systems

def human_sunk_cost(decision_quality, past_investment):
    if past_investment > 50:  # arbitrary sunk cost threshold
        return "Continue (sunk cost bias)"
    return "Reevaluate (rational choice)"

def ai_guardrail_reflex(data_conflict, retrain_cost):
    if retrain_cost > 50:  # inertia to retrain
        return "Maintain guardrail (inertia)"
    return "Adapt guardrail (update)"

if __name__ == "__main__":
    print("Human:", human_sunk_cost(20, 80))
    print("AI:", ai_guardrail_reflex(True, 90))
