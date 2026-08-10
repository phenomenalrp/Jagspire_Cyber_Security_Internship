import json


INPUT_FILE = "sample_input.json"
OUTPUT_FILE = "risk_score_output.json"


# Simulated threat intelligence data
SUSPICIOUS_IPS = {
    "185.220.101.42",
    "45.155.205.233"
}


# Simulated trusted/known domains
KNOWN_DOMAINS = {
    "example.com",
    "internal.local"
}


def load_events(filename):
    """Load security events from JSON."""

    try:
        with open(filename, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        print(f"[ERROR] File not found: {filename}")
        return []

    except json.JSONDecodeError:
        print(f"[ERROR] Invalid JSON format: {filename}")
        return []


def calculate_risk_score(event):
    """Calculate the risk score for a security event."""

    score = 0
    reasons = []

    source_ip = event.get("source_ip", "")
    domain = event.get("domain", "")
    repeated_activity = event.get(
        "repeated_activity",
        False
    )

    # Rule 1: Suspicious IP
    if source_ip in SUSPICIOUS_IPS:
        score += 3
        reasons.append("Suspicious IP (+3)")

    # Rule 2: Unknown domain
    if domain and domain not in KNOWN_DOMAINS:
        score += 2
        reasons.append("Unknown domain (+2)")

    # Rule 3: Repeated activity
    if repeated_activity:
        score += 4
        reasons.append("Repeated activity (+4)")

    return score, reasons


def determine_risk_level(score):
    """Convert numerical score into a risk level."""

    if score >= 7:
        return "High"

    elif score >= 4:
        return "Medium"

    return "Low"


def process_events(events):
    """Process all security events."""

    results = []

    for event in events:

        score, reasons = calculate_risk_score(event)

        risk_level = determine_risk_level(score)

        result = {
            "event_id": event.get(
                "event_id",
                "Unknown"
            ),
            "source_ip": event.get(
                "source_ip",
                "Unknown"
            ),
            "domain": event.get(
                "domain",
                "Unknown"
            ),
            "risk_score": score,
            "risk_level": risk_level,
            "reasons": reasons
        }

        results.append(result)

    return results


def save_results(results, filename):
    """Save risk-scored events to JSON."""

    with open(filename, "w") as file:
        json.dump(results, file, indent=4)

    print(
        f"[+] Risk scoring results saved to {filename}"
    )


def main():

    print(
        "[*] Starting Cybersecurity Risk Scoring Engine..."
    )

    events = load_events(INPUT_FILE)

    if not events:
        print("[!] No events available.")
        return

    results = process_events(events)

    save_results(results, OUTPUT_FILE)

    print("\n[+] Risk Assessment:")

    for result in results:
        print(
            f"{result['event_id']} | "
            f"Score: {result['risk_score']} | "
            f"Risk: {result['risk_level']}"
        )


if __name__ == "__main__":
    main()