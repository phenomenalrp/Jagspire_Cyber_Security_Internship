# AI Security Data Processing Engine

## Overview

The AI Security Data Processing Engine is a Python-based mini security pipeline developed as part of the Jagspire Cyber Security Internship – Week 2.

The project combines log ingestion, threat enrichment, rule-based risk scoring, and basic anomaly detection into a single processing workflow.

## Objectives

* Ingest security logs from JSON
* Enrich events with threat intelligence context
* Identify suspicious IPs and domains
* Calculate risk scores
* Detect anomalous login behavior
* Generate a structured security report

## Processing Pipeline

```text
Security Logs
      ↓
Log Ingestion
      ↓
Threat Enrichment
      ↓
Risk Scoring
      ↓
Anomaly Detection
      ↓
Security Report
```

## Features

### 1. Log Ingestion

The engine reads security events from a JSON input file.

### 2. Threat Enrichment

Events are enriched using a demonstration threat-intelligence dataset containing suspicious IP addresses and domains.

### 3. Risk Scoring

The project uses a simple rule-based scoring model:

| Indicator                 | Score |
| ------------------------- | ----: |
| Suspicious IP             |    +3 |
| Suspicious/unknown domain |    +2 |
| Repeated activity         |    +4 |
| Failed login              |    +1 |

Risk levels:

| Score | Level  |
| ----: | ------ |
|   0–3 | Low    |
|   4–6 | Medium |
|    7+ | High   |

These values are project-defined for demonstration purposes.

### 4. Anomaly Detection

The system identifies suspicious behavior such as:

* Repeated failed login attempts
* Unusual login activity
* High activity from a single IP

### 5. Report Generation

The processed events are stored in a structured JSON security report containing:

* Risk score
* Risk level
* Threat indicators
* Anomaly status
* Detection reasons

## Project Structure

```text
Day_14/
├── security_engine.py
├── sample_input.json
├── security_report.json
└── Day_14.md
```

## Example

A suspicious event may contain:

```text
Source IP: 45.155.205.233
Domain: unknown-login.com
Status: failed
```

The engine identifies:

```text
Suspicious IP        +3
Suspicious Domain    +2
Repeated Activity    +4
Failed Login         +1

Risk Score: 10
Risk Level: HIGH
Anomaly: TRUE
```
## Final Project Architecture

                 ┌──────────────────┐
                 │  Security Logs   │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │  Log Ingestion   │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Threat Enrichment│
                 │ IP / Domain / IOC│
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │   Risk Scoring   │
                 │ Score + Severity │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Anomaly Detection│
                 │ Behavior Analysis│
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Security Report  │
                 └──────────────────┘

## Technologies

* Python 3
* JSON
* Python Collections module
* Rule-based threat detection

## Limitations

This project is an educational prototype and does not represent a production SOC platform.

Current limitations include:

* Static JSON input
* Demonstration threat-intelligence data
* Rule-based risk scoring
* Basic anomaly detection
* No real-time log ingestion
* No trained machine-learning model
* No database

## Future Improvements

Possible improvements include:

* Connect real CTI feeds/APIs
* Add GeoIP enrichment
* Integrate a SIEM
* Use a database for event storage
* Implement real-time log ingestion
* Add machine-learning anomaly detection
* Add a frontend SOC dashboard
* Add authentication and API security

## Learning Outcome

This project provided practical experience with processing security logs, enriching threat data, prioritizing security events using risk scores, and identifying abnormal behavior.

It demonstrates the basic architecture of a security data processing pipeline that can serve as a foundation for more advanced SOC and AI-based security systems.