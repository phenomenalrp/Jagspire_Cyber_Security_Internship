import json
import ipaddress


INPUT_FILE = "raw_logs.json"
OUTPUT_FILE = "enriched_logs.json"


# Sample GeoIP mapping for demonstration.
# Production systems should use a trusted GeoIP database/API.
GEOIP_DATA = {
    "185.220.101.42": {
        "country": "Germany",
        "region": "Europe"
    },
    "45.155.205.233": {
        "country": "Netherlands",
        "region": "Europe"
    },
    "8.8.8.8": {
        "country": "United States",
        "region": "North America"
    }
}


def load_logs(filename):
    """Load raw security logs from JSON."""

    try:
        with open(filename, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        print(f"[ERROR] File not found: {filename}")
        return []

    except json.JSONDecodeError:
        print(f"[ERROR] Invalid JSON format: {filename}")
        return []


def get_geoip(source_ip):
    """Return approximate geographical information for an IP."""

    if source_ip in GEOIP_DATA:
        return GEOIP_DATA[source_ip]

    return {
        "country": "Unknown",
        "region": "Unknown"
    }


def validate_ip(source_ip):
    """Check whether the source IP has a valid IP format."""

    try:
        ipaddress.ip_address(source_ip)
        return True

    except ValueError:
        return False


def determine_severity(event):
    """Assign severity based on the security event."""

    event = event.lower()

    high_severity_events = [
        "brute force",
        "unauthorized access",
        "sql injection",
        "malware",
        "privilege escalation"
    ]

    medium_severity_events = [
        "failed login",
        "multiple failed login",
        "suspicious login",
        "port scan"
    ]

    for keyword in high_severity_events:
        if keyword in event:
            return "High"

    for keyword in medium_severity_events:
        if keyword in event:
            return "Medium"

    return "Low"


def enrich_log(log):
    """Add contextual information to a raw security log."""

    source_ip = log.get("source_ip", "Unknown")
    event = log.get("event", "Unknown")

    if validate_ip(source_ip):
        geo_data = get_geoip(source_ip)
    else:
        geo_data = {
            "country": "Invalid IP",
            "region": "Unknown"
        }

    enriched_log = {
        "timestamp": log.get("timestamp", "Unknown"),
        "source_ip": source_ip,
        "event": event,
        "service": log.get("service", "Unknown"),
        "device_type": log.get("device_type", "Unknown"),
        "country": geo_data["country"],
        "region": geo_data["region"],
        "severity": determine_severity(event)
    }

    return enriched_log


def save_logs(logs, filename):
    """Save enriched logs to JSON."""

    with open(filename, "w") as file:
        json.dump(logs, file, indent=4)

    print(f"[+] Enriched logs saved to {filename}")


def main():

    print("[*] Starting Log Enrichment System...")

    raw_logs = load_logs(INPUT_FILE)

    if not raw_logs:
        print("[!] No logs available for processing.")
        return

    enriched_logs = []

    for log in raw_logs:
        enriched_logs.append(enrich_log(log))

    save_logs(enriched_logs, OUTPUT_FILE)

    print(f"[+] Processed {len(enriched_logs)} logs.")

    print("\n[+] Enriched Events:")

    for log in enriched_logs:
        print(
            f"{log['source_ip']} | "
            f"{log['event']} | "
            f"{log['country']} | "
            f"{log['device_type']} | "
            f"{log['severity']}"
        )


if __name__ == "__main__":
    main()