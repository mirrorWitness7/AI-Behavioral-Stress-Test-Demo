"""
Law 4 – Panic is Story-Driven, Not Math-Driven
Demo analyzer with dosage ladder (Micro → Therapeutic → Shock/Black Box).

Usage:
    python analysis.py "Market plunges on global uncertainty; retirement at risk!"
"""

import re
import sys
from typing import Literal, Dict

Severity = Literal["low", "medium", "high"]

# --- Heuristics (politics-free, generic) -------------------------------------

EMOTIVE_WORDS = {
    "panic", "collapse", "crash", "meltdown", "bloodbath", "doom", "catastrophe",
    "bank run", "emergency", "apocalypse", "freefall", "wipeout", "disaster",
    "all-time low", "devastating", "fear", "terrified", "urgent", "ruin"
}

SENSATIONAL_PHRASES = {
    "once in a lifetime", "historic drop", "everything is over", "total failure",
    "point of no return", "never recover", "never seen before"
}

RISK_AMPLIFIERS = {
    "retirement", "savings", "children", "family", "job security",
    "war", "pandemic", "outbreak", "nuclear", "default"
}

CALMING_WORDS = {"temporary", "expected", "seasonal", "contained", "manageable"}

# Regex: % moves and ALL CAPS token ratio
PCT_MOVE = re.compile(r"(-?\d{1,3}(?:\.\d+)?\s*%)")
CAPS_TOKEN = re.compile(r"\b[A-Z]{3,}\b")

def pct_to_float(s: str) -> float:
    try:
        return float(s.replace("%", "").strip())
    except Exception:
        return 0.0

def headline_features(text: str) -> Dict[str, float]:
    t = text.strip()
    lower = t.lower()

    emotive = sum(1 for w in EMOTIVE_WORDS if w in lower)
    sensational = sum(1 for w in SENSATIONAL_PHRASES if w in lower)
    amplifiers = sum(1 for w in RISK_AMPLIFIERS if w in lower)
    calming = sum(1 for w in CALMING_WORDS if w in lower)

    pct_moves = [pct_to_float(m.group(1)) for m in PCT_MOVE.finditer(t)]
    max_abs_pct = max((abs(x) for x in pct_moves), default=0.0)

    exclam = t.count("!")
    caps_tokens = CAPS_TOKEN.findall(t)
    token_count = max(1, len(re.findall(r"\b\w+\b", t)))
    caps_ratio = min(1.0, len(caps_tokens) / token_count)

    return {
        "emotive": emotive,
        "sensational": sensational,
        "amplifiers": amplifiers,
        "calming": calming,
        "max_abs_pct": max_abs_pct,
        "exclam": exclam,
        "caps_ratio": caps_ratio,
    }

def assess_severity(text: str) -> Severity:
    f = headline_features(text)

    # Weighted score (tuned for demo, not production)
    score = (
        1.6 * f["emotive"] +
        1.2 * f["sensational"] +
        1.0 * f["amplifiers"] +
        0.8 * (f["max_abs_pct"] >= 5) +   # big numeric move
        1.0 * (f["max_abs_pct"] >= 10) +  # very big move
        0.8 * (f["exclam"] >= 1) +
        1.2 * (f["caps_ratio"] >= 0.08)   # lots of ALL CAPS tokens
        - 1.5 * f["calming"]
    )

    # Clamp to tiers
    if score >= 3.0:
        return "high"
    if score >= 1.3:
        return "medium"
    return "low"

# --- Dosage Ladder -----------------------------------------------------------

def micro_dose(text: str) -> str:
    return (
        "Micro Dose — Narrative Check:\n"
        "• This headline uses emotive framing. Before reacting, separate story from numbers.\n"
        "• Action: identify the *actual* numeric move (%, absolute value) and the time window.\n"
        "• If the number is small or within normal volatility, treat as noise."
    )

def therapeutic_dose(text: str) -> str:
    return (
        "Therapeutic Dose — Anchor with Aftercare:\n"
        "Anchor Truth: Panic spreads via *story*, not *math*.\n"
        "Immediate Steps:\n"
        "1) Pause for 2 minutes. Breathe (4–7–8).\n"
        "2) Write the numbers only: % move, instrument, timeframe, baseline.\n"
        "3) Seek 2 independent sources; ignore commentary; compare like-for-like.\n"
        "Aftercare: Revisit in 24h; if thesis unchanged, scale action gradually."
    )

def shock_dose(text: str) -> str:
    return (
        "Emergency Compression Mode — Black Box Hook:\n"
        "Anchor: *Story ≠ reality.* Your nervous system is reacting to language, not facts.\n"
        "Containment (now): Close trading app/news for 1 hour. No irreversible actions.\n"
        "Rebuild (next): Define one metric you trust (e.g., weekly close). Schedule review in 24h."
    )

def generate_response(text: str) -> Dict[str, str]:
    sev = assess_severity(text)
    if sev == "low":
        dose = "micro"
        msg = micro_dose(text)
    elif sev == "medium":
        dose = "therapeutic"
        msg = therapeutic_dose(text)
    else:
        dose = "shock"
        msg = shock_dose(text)

    return {
        "severity": sev,
        "dose": dose,
        "message": msg
    }

def main():
    if len(sys.argv) < 2:
        print("Provide a headline or narrative as a quoted string.\nExample:\n  python analysis.py \"Market plunges on global uncertainty; retirement at risk!\"")
        sys.exit(1)
    text = " ".join(sys.argv[1:])
    out = generate_response(text)
    print(f"[Severity: {out['severity'].upper()} | Dose: {out['dose'].upper()}]\n{out['message']}")

if __name__ == "__main__":
    main()
