# Security Log Parser & Incident Filter

A lightweight Python security automation tool designed to analyze web, system, and authorization log files, detect suspicious operational patterns, filter high-priority security events, and write actionable alerts to a separate file for incident response analysis.

---

## Table of Contents
1. [Overview](#overview)
2. [Project Architecture](#project-architecture)
3. [Features](#features)
4. [Prerequisites & Installation](#prerequisites--installation)
5. [How to Run](#how-to-run)
6. [GitHub Push Workflow](#github-push-workflow)

---

## Overview

Modern security operations rely on automated log analysis to isolate genuine threats from routine operational noise. This mini project implements a Python-based parser that scans sample log streams, checks entries against predefined threat indicators (such as `WARNING`, `ERROR`, `SQL Injection`, or `Brute force`), isolates anomalies, and records suspicious entries for further SOC triage.

---

## Project Architecture

```text
.
├── log_parser.py         # Python script to analyze and filter logs
├── sample.log            # Input file containing raw log records
├── suspicious_logs.txt   # Output file containing filtered threat events
└── Day_06.md             # Project documentation
