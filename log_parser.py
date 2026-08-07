import os

LOG_FILE = "sample.log"
OUTPUT_FILE = "suspicious_logs.txt"

SUSPICIOUS_KEYWORDS = [
    "WARNING",
    "ERROR",
    "failed login",
    "Brute Force",
    "SQL Injection",
    "Unauthorized",
    "Port scanning"
]

try:
    with open(LOG_FILE, "r") as log_file:
        logs = log_file.readlines()

    suspicious_logs = []

    for log in logs:
        if any(keyword.lower() in log.lower() for keyword in SUSPICIOUS_KEYWORDS):
            suspicious_logs.append(log.strip())

    with open(OUTPUT_FILE, "w") as output:
        output.write("=== Suspicious Log Report ===\n\n")

        if suspicious_logs:
            for log in suspicious_logs:
                output.write(log + "\n")
        else:
            output.write("No suspicious logs found.")

    print(f"Analysis completed.")
    print(f"Total logs: {len(logs)}")
    print(f"Suspicious logs: {len(suspicious_logs)}")
    print(f"Report saved as '{OUTPUT_FILE}'")

except FileNotFoundError:
    print("Error: sample.log not found.")