# Day 11 – Mini SOC Dashboard Backend

## Overview

This project implements the backend logic for a basic Security Operations Center (SOC) dashboard using Python and JSON-based storage.

The system stores security events, aggregates event statistics, filters events by severity, and identifies the top 10 highest-risk threats.

## Objectives

* Understand basic SOC dashboard components
* Store security events in structured JSON
* Aggregate security events
* Filter events by severity
* Identify the highest-risk events
* Generate dashboard-ready JSON data

## Features

### 1. Log Storage

Security events are stored in:

```text
security_logs.json
```

### 2. Event Aggregation

The backend calculates:

* Total events
* High-severity events
* Medium-severity events
* Low-severity events

### 3. Severity Filtering

Events can be filtered by:

* High
* Medium
* Low

### 4. Top 10 Threats

Events are sorted according to their risk score, and the 10 highest-risk events are selected.

## Processing Flow

```text
Security Logs
      ↓
JSON Storage
      ↓
Event Aggregation
      ↓
Severity Filtering
      ↓
Risk Score Sorting
      ↓
Top 10 Threats
      ↓
Dashboard JSON
```

## Project Structure

```text
day11_soc_dashboard/
├── soc_dashboard.py
├── security_logs.json
├── dashboard_output.json
└── Day_11.md
```

## Technologies Used

* Python 3
* JSON
* Python built-in modules

## Sample Summary

```text
Total Events : 8
High         : 4
Medium       : 1
Low          : 3
```

## Sample Top Threats

```text
EVT001 | 185.220.101.42 | Risk: 9 | High
EVT006 | 185.220.101.42 | Risk: 9 | High
EVT003 | 45.155.205.233 | Risk: 8 | High
EVT008 | 45.155.205.233 | Risk: 7 | High
```

## How to Run

```bash
python3 soc_dashboard.py
```

## Security Relevance

SOC dashboards help analysts monitor and prioritize security events. Aggregating events by severity and displaying the highest-risk threats allows analysts to focus their attention on potentially important incidents.

This backend can serve as the foundation for a future graphical dashboard or web-based SOC monitoring interface.

## Limitations

* JSON is used as a simple storage mechanism for this learning project.
* No graphical interface is implemented.
* The system processes a static dataset rather than a live log stream.
* Authentication and access control are not included because this task focuses on backend dashboard logic.

## Learning Outcome

Learned how SOC dashboard backends aggregate security events, filter alerts by severity, and prioritize high-risk threats for analyst investigation.