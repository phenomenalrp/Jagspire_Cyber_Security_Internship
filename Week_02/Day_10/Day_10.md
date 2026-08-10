# Day 10 – Basic Cybersecurity Risk Scoring Engine

## Overview

This project implements a basic rule-based cybersecurity risk scoring engine using Python.

The system evaluates security events based on predefined indicators and assigns a numerical risk score and risk level.

## Objectives

* Understand risk scoring in cybersecurity
* Understand rule-based vs AI-based scoring
* Assign numerical scores to suspicious events
* Explain why an event received a particular score
* Prioritize security events based on risk

## Scoring Rules

| Condition         | Score |
| ----------------- | ----: |
| Suspicious IP     |    +3 |
| Unknown domain    |    +2 |
| Repeated activity |    +4 |

## Risk Levels

For this project:

```text
0–3  → Low
4–6  → Medium
7+   → High
```

These thresholds are project-defined and are not universal cybersecurity standards.

## Processing Flow

```text
Security Event
      ↓
Check Suspicious IP
      ↓
Check Unknown Domain
      ↓
Check Repeated Activity
      ↓
Calculate Total Score
      ↓
Assign Risk Level
      ↓
Generate Explanation
```

## Project Structure

```text
day10_risk_scoring/
├── risk_scoring.py
├── sample_input.json
├── risk_score_output.json
└── README.md
```

## Technologies Used

* Python 3
* JSON
* Rule-based scoring

## Sample Output

```text
EVT001 | Score: 9 | Risk: High
EVT002 | Score: 0 | Risk: Low
EVT003 | Score: 5 | Risk: Medium
EVT004 | Score: 6 | Risk: Medium
```

## Rule-Based vs AI-Based Scoring

This implementation uses rule-based scoring. The score is determined using predefined conditions.

For example:

```text
Suspicious IP → +3
Unknown domain → +2
Repeated activity → +4
```

An AI/ML-based system would instead learn patterns from historical security data and use those patterns to estimate the likelihood or risk of an event.

## Explainability

The system records the reasons contributing to each score. This allows a SOC analyst to understand why an event was classified as high, medium, or low risk.

## Limitations

* The suspicious IP list is a small simulated threat-intelligence dataset.
* The known-domain list is manually defined.
* Repeated activity is provided as an input rather than calculated from historical events.
* The scoring system is rule-based and does not use machine learning.
* Risk thresholds are defined specifically for this project.

## Security Relevance

Risk scoring can help SOC analysts prioritize alerts. Higher-risk events can be investigated first, while lower-risk events can receive less immediate attention.

This module can consume enriched security events from the Day 9 Log Enrichment System and can later be integrated into the Week 2 security-processing pipeline.

## Learning Outcome

Learned how cybersecurity risk scoring can be implemented using predefined security rules and how explainable scoring can help SOC analysts prioritize security events.