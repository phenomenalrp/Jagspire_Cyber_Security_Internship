import json


LOG_FILE = "security_logs.json"
OUTPUT_FILE = "dashboard_output.json"


def load_logs(filename):
    """Load security logs from JSON."""

    try:
        with open(filename, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        print(f"[ERROR] File not found: {filename}")
        return []

    except json.JSONDecodeError:
        print(f"[ERROR] Invalid JSON format: {filename}")
        return []


def filter_by_severity(logs, severity):
    """Return logs matching the requested severity."""

    return [
        log for log in logs
        if log.get("severity", "").lower() == severity.lower()
    ]


def get_top_threats(logs, limit=10):
    """Return the highest-risk events."""

    return sorted(
        logs,
        key=lambda log: log.get("risk_score", 0),
        reverse=True
    )[:limit]


def aggregate_events(logs):
    """Generate summary statistics."""

    summary = {
        "total_events": len(logs),
        "high": 0,
        "medium": 0,
        "low": 0
    }

    for log in logs:
        severity = log.get("severity", "").lower()

        if severity == "high":
            summary["high"] += 1

        elif severity == "medium":
            summary["medium"] += 1

        elif severity == "low":
            summary["low"] += 1

    return summary


def create_dashboard_data(logs):
    """Build dashboard-ready backend data."""

    summary = aggregate_events(logs)

    high_events = filter_by_severity(logs, "High")
    medium_events = filter_by_severity(logs, "Medium")
    low_events = filter_by_severity(logs, "Low")

    top_threats = get_top_threats(logs)

    return {
        "summary": summary,
        "severity_events": {
            "high": high_events,
            "medium": medium_events,
            "low": low_events
        },
        "top_10_threats": top_threats
    }


def save_dashboard_data(data, filename):
    """Save dashboard data to JSON."""

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    print(f"[+] Dashboard data saved to {filename}")


def main():

    print("[*] Starting Mini SOC Dashboard Backend...")

    logs = load_logs(LOG_FILE)

    if not logs:
        print("[!] No security logs available.")
        return

    dashboard_data = create_dashboard_data(logs)

    save_dashboard_data(
        dashboard_data,
        OUTPUT_FILE
    )

    print("\n[+] SOC Event Summary")

    summary = dashboard_data["summary"]

    print(f"Total Events : {summary['total_events']}")
    print(f"High         : {summary['high']}")
    print(f"Medium       : {summary['medium']}")
    print(f"Low          : {summary['low']}")

    print("\n[+] Top Threats")

    for threat in dashboard_data["top_10_threats"]:
        print(
            f"{threat['event_id']} | "
            f"{threat['source_ip']} | "
            f"{threat['event']} | "
            f"Risk: {threat['risk_score']} | "
            f"{threat['severity']}"
        )


if __name__ == "__main__":
    main()