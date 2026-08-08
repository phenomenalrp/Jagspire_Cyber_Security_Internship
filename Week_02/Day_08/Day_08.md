# Day 8 – Threat Intelligence & Data Collection Module

## Overview

This project implements a basic Threat Intelligence and Data Collection module using Python.

The module reads threat intelligence data from a structured JSON dataset, identifies different types of Indicators of Compromise (IOCs), and generates a structured output file that can be used by later security-processing modules.

## Objectives

* Understand the basics of Cyber Threat Intelligence (CTI)
* Work with structured security data
* Identify common IOC types
* Process threat intelligence using Python
* Store security indicators in JSON format
* Implement basic error handling

## IOC Types

The project identifies:

* IP addresses
* Domains
* URLs
* Unknown indicators

## Project Structure

```text
day08_threat_intelligence/
├── threat_intel.py
├── sample_threat_data.json
├── structured_threat_data.json
└── Day_08.md
```

## How It Works

```text
Threat Intelligence Dataset
          ↓
      JSON Input
          ↓
     Python Parser
          ↓
      IOC Detection
          ↓
    Structured JSON
```

## Technologies Used

* Python 3
* JSON
* Regular Expressions
* Git/GitHub

## How to Run

Clone the repository and navigate to the project directory:

```bash
cd Day_08
```

Run the Python script:

```bash
python3 threat_intel.py
```

## Sample Output

```text
[*] Starting Threat Intelligence Collector...
[+] Structured data saved to structured_threat_data.json
[+] Processed 5 indicators.

[+] Identified IOCs:
    IP      185.220.101.42
    IP      45.155.205.233
    DOMAIN  malicious-example.com
    DOMAIN  updates-example.net
    URL     http://evil-example.org/login
```

## Security Relevance

Threat Intelligence provides security teams with information about potentially malicious indicators such as IP addresses, domains, and URLs.

In a SOC environment, these indicators can be used to enrich alerts, investigate suspicious activity, correlate events, and prioritize potential threats.

## Limitations

This implementation uses a mock threat-intelligence dataset rather than a live external feed.

IOC detection is based on pattern matching and does not determine whether an indicator is actually malicious. A production system would require trusted threat-intelligence feeds, IOC validation, reputation data, and additional security controls.

## Future Improvements

* Integrate a public threat-intelligence API
* Use Python's `ipaddress` module for IP validation
* Add IOC reputation checking
* Add duplicate IOC detection
* Add timestamps and confidence scores
* Connect the output to the Week 2 log-enrichment module

## Learning Outcome

Through this task, I learned how threat-intelligence data can be collected, structured, classified, and prepared for further security analysis.
