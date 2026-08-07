# Day 2: Cybersecurity Fundamentals & Frameworks

A comprehensive overview of foundational cybersecurity concepts, attack frameworks, vulnerability standards, security operational models, and threat intelligence workflows.

---

## Table of Contents
1. [Cyber Kill Chain](#1-cyber-kill-chain)
2. [MITRE ATT&CK Framework](#2-mitre-attck-framework)
3. [OWASP Top 10 (2025)](#3-owasp-top-10-2025)
4. [The CIA Triad](#4-the-cia-triad)
5. [SOC Workflow & Tools](#5-soc-workflow--tools)
6. [Threat Intelligence Basics](#6-threat-intelligence-basics)

---

## 1. Cyber Kill Chain

Developed by **Lockheed Martin**, the Cyber Kill Chain framework outlines the sequential stages of a targeted cyber attack. Understanding these stages helps security teams detect, prevent, and stop adversary operations before objectives are met.

### The 7 Stages
1. **Reconnaissance:** Researching, identifying, and selecting targets (e.g., harvesting email addresses or scanning network ranges).
2. **Weaponization:** Coupling malware with an exploit into a deliverable payload (e.g., creating an infected PDF or weaponized Office document).
3. **Delivery:** Transmitting the weaponized payload to the target (e.g., via phishing emails or malicious web pages).
4. **Exploitation:** Triggering the payload code to exploit a vulnerability on the target system.
5. **Installation:** Installing malware, backdoors, or remote access tools on the compromised asset.
6. **Command & Control (C2):** Establishing a secure communication channel between the compromised host and the attacker's external server.
7. **Actions on Objectives:** Executing the primary attack goals (e.g., data exfiltration, encryption, or system destruction).

---

## 2. MITRE ATT&CK Framework

The **MITRE ATT&CK** (Adversarial Tactics, Techniques, and Common Knowledge) framework is a globally accessible, living knowledge base of real-world adversary tactics and techniques.

### Core Tactics
* **Reconnaissance:** Gathering information to plan future operations.
* **Resource Development:** Establishing infrastructure, accounts, and capabilities.
* **Initial Access:** Gaining an initial foothold within a network.
* **Execution:** Running malicious code or scripts.
* **Persistence:** Maintaining access across restarts and credential changes.
* **Privilege Escalation:** Gaining higher-level permissions (e.g., root or SYSTEM).
* **Stealth:** Evading active defenses and security controls.
* **Defense Impairment:** Disabling or tampering with security mechanisms.
* **Credential Access:** Stealing account names and passwords.
* **Discovery:** Exploring and mapping the target environment.
* **Lateral Movement:** Moving through the network to access additional assets.
* **Collection:** Gathering target data of interest.
* **Command & Control:** Communicating with controlled systems over external channels.
* **Exfiltration:** Stealing and exfiltrating data out of the network.
* **Impact:** Manipulating, interrupting, or destroying systems and data.

---

## 3. OWASP Top 10 (2025)

The **OWASP Top 10** is a globally recognized awareness standard representing the most critical security risks facing web applications.

### 2025 Critical Vulnerabilities
1. **Broken Access Control**
2. **Security Misconfiguration**
3. **Software Supply Chain Failures**
4. **Cryptographic Failures**
5. **Injection**
6. **Insecure Design**
7. **Authentication Failures**
8. **Software & Data Integrity Failures**
9. **Security Logging and Alerting Failures**
10. **Mishandling of Exceptional Conditions**

---

## 4. The CIA Triad

The **CIA Triad** is the core foundational security model used to safeguard data, restrict unauthorized access, and ensure reliable system operation.

### Key Pillars
* **Confidentiality:** Ensuring data remains private and accessible only to authorized personnel.
* **Integrity:** Protecting data from unauthorized modification, tampering, or deletion.
* **Availability:** Ensuring critical systems, applications, and data are consistently accessible to legitimate users when needed.

---

## 5. SOC Workflow & Tools

A **Security Operations Center (SOC)** workflow is a continuous 6-stage lifecycle used by analysts to identify, triage, and neutralize threats.

### Core Stages
1. **Preparation / Alert:** Receiving and triggering alerts from security monitoring software.
2. **Triage:** Categorizing, evaluating, and determining the severity of an incoming alert.
3. **Investigation:** Analyzing system logs, network traffic, and artifacts to confirm malicious activity.
4. **Containment:** Isolating affected hosts or systems to prevent lateral movement.
5. **Remediation:** Eliminating threats (e.g., removing malware, patching vulnerabilities) and restoring operational status.
6. **Report:** Documenting the incident, root cause, timeline, and remediation actions for continuous improvement.

### Essential Enterprise SOC Tools
* **Splunk** (SIEM)
* **Wazuh** (Open-Source SIEM / XDR)
* **Microsoft Defender** (EDR / XDR)
* **Microsoft Sentinel** (Cloud SIEM)
* **IBM QRadar** (SIEM)

---

## 6. Threat Intelligence Basics

**Threat Intelligence** is evidence-based knowledge—including context, mechanisms, indicators, implications, and actionable advice—about existing or emerging cyber threats.

### The Threat Intelligence Lifecycle
1. **Requirements:** Defining objectives, scope, and key intelligence priorities.
2. **Collection:** Gathering raw security data from technical feeds, dark web forums, and internal logs.
3. **Processing:** Structuring, filtering, and organizing raw data into usable formats.
4. **Analysis:** Converting processed data into actionable threat insight.
5. **Dissemination:** Delivering finished threat intelligence to stakeholders and security teams.
6. **Feedback:** Evaluating performance and refining intelligence requirements for future cycles.
