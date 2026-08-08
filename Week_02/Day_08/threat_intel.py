import json
import re
from pathlib import Path


INPUT_FILE = "sample_threat_data.json"
OUTPUT_FILE = "structured_threat_data.json"


def load_threat_data(filename):
    """Load threat intelligence data from a JSON file."""
    try:
        with open(filename, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        print(f"[ERROR] File not found: {filename}")
        return []

    except json.JSONDecodeError:
        print(f"[ERROR] Invalid JSON format in: {filename}")
        return []


def identify_ioc_type(indicator):
    """Identify whether an indicator is an IP, domain, or URL."""

    ip_pattern = r"^(?:\d{1,3}\.){3}\d{1,3}$"

    domain_pattern = (
        r"^(?:[a-zA-Z0-9-]+\.)+"
        r"[a-zA-Z]{2,}$"
    )

    url_pattern = r"^https?://"

    if re.match(ip_pattern, indicator):
        return "ip"

    elif re.match(url_pattern, indicator):
        return "url"

    elif re.match(domain_pattern, indicator):
        return "domain"

    return "unknown"


def process_threat_data(threat_data):
    """Process and structure threat intelligence records."""

    structured_data = []

    for item in threat_data:

        indicator = item.get("indicator", "").strip()

        if not indicator:
            continue

        ioc_type = identify_ioc_type(indicator)

        record = {
            "indicator": indicator,
            "ioc_type": ioc_type,
            "threat": item.get("threat", "Unknown"),
            "severity": item.get("severity", "unknown"),
            "source": item.get(
                "source",
                "Unknown"
            )
        }

        structured_data.append(record)

    return structured_data


def save_threat_data(data, filename):
    """Save processed threat intelligence to JSON."""

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    print(f"[+] Structured data saved to {filename}")


def main():

    print("[*] Starting Threat Intelligence Collector...")

    threat_data = load_threat_data(INPUT_FILE)

    if not threat_data:
        print("[!] No threat intelligence data found.")
        return

    structured_data = process_threat_data(threat_data)

    save_threat_data(structured_data, OUTPUT_FILE)

    print(f"[+] Processed {len(structured_data)} indicators.")

    print("\n[+] Identified IOCs:")

    for item in structured_data:
        print(
            f"    {item['ioc_type'].upper():7} "
            f"{item['indicator']}"
        )


if __name__ == "__main__":
    main()