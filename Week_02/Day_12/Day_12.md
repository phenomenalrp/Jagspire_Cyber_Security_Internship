# Day 12 – Introduction to AI in Cyber Security

## Overview

This project implements a simple cybersecurity anomaly detector using Python.

The system analyzes login activity and identifies potentially abnormal behavior based on predefined behavioral thresholds.

## Objectives

* Understand how AI can be used in cybersecurity
* Understand anomaly detection
* Identify unusual login activity
* Detect repeated failed access
* Identify abnormal IP behavior
* Generate an anomaly report

## Detection Rules

| Behavior               |               Threshold |
| ---------------------- | ----------------------: |
| Unusual login activity |      More than 5 events |
| Repeated failed access | 3 or more failed logins |
| Abnormal IP activity   |       10 or more events |

These thresholds are project-defined for demonstration and are not universal security standards.

## Detection Flow

```text
Security Logs
      ↓
Count IP Activity
      ↓
Count Failed Logins
      ↓
Apply Detection Rules
      ↓
Identify Anomalies
      ↓
Generate JSON Report
```

## Project Structure

```text
Day_12/
├── anomaly_detector.py
├── sample_logs.json
├── anomaly_report.json
└── Day_12.md
```

## Technologies Used

* Python 3
* JSON
* Python Collections module
* Rule-based anomaly detection

## Sample Detection

For example, if an IP generates six failed login attempts:

```text
IP: 45.155.205.233
Total Events: 6
Failed Logins: 6

Detected:
- Unusual login activity
- Repeated failed access
```

## Rule-Based vs AI-Based Detection

This project uses predefined behavioral thresholds rather than a trained machine-learning model.

A production AI/ML anomaly detection system could learn normal behavior from historical security data and identify deviations automatically.

## Security Relevance

Anomaly detection can help SOC analysts identify unusual authentication behavior, possible brute-force attacks, compromised accounts, and abnormal network activity.

## Limitations

* Detection thresholds are manually defined.
* The dataset is static.
* No machine-learning model is used.
* The system does not perform real-time monitoring.
* An anomaly does not necessarily mean an attack; it requires further investigation.

## Learning Outcome

Learned how anomaly detection can be applied to security logs to identify unusual authentication behavior and how behavioral patterns can assist SOC analysts in detecting potential threats.
