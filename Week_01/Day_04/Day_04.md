# Day 4: Networking Fundamentals, Wireshark & Basic Log Analysis

A practical guide covering networking core concepts, Wireshark packet capture analysis, log analysis methodologies, system event triage, and hands-on exercises[cite: 3].

---

## Table of Contents
1. [Basic Networking Concepts](#1-basic-networking-concepts)
2. [Wireshark Basics](#2-wireshark-basics)
3. [Basic Log Analysis](#3-basic-log-analysis)
4. [Understanding System & Network Events](#4-understanding-system--network-events)
5. [Practical Exercises](#5-practical-exercises)

---

## 1. Basic Networking Concepts

### IP Address
A unique identifier assigned to a device on a network[cite: 3].
* **IPv4:** `192.168.1.10`[cite: 3]
* **IPv6:** `2001:db8::1`[cite: 3]

### DNS (Domain Name System)
Converts domain names into IP addresses[cite: 3].
* **Example:** `google.com` → `142.250.x.x`[cite: 3]

### HTTP vs. HTTPS

| Feature | HTTP | HTTPS |
| :--- | :--- | :--- |
| **Port** | Port 80[cite: 3] | Port 443[cite: 3] |
| **Encryption** | Unencrypted[cite: 3] | Encrypted (TLS/SSL)[cite: 3] |
| **Security** | Less secure[cite: 3] | Secure[cite: 3] |

### Common Ports

| Port | Service[cite: 3] |
| :--- | :--- |
| **20 / 21** | FTP[cite: 3] |
| **22** | SSH[cite: 3] |
| **23** | Telnet[cite: 3] |
| **25** | SMTP[cite: 3] |
| **53** | DNS[cite: 3] |
| **80** | HTTP[cite: 3] |
| **110** | POP3[cite: 3] |
| **143** | IMAP[cite: 3] |
| **443** | HTTPS[cite: 3] |
| **3389** | RDP[cite: 3] |

---

## 2. Wireshark Basics

### What is Wireshark?
A network protocol analyzer used to capture and inspect network traffic[cite: 3].

### Common Display Filters
* `ip.addr == 192.168.1.10`[cite: 3]
* `http`[cite: 3]
* `dns`[cite: 3]
* `tcp.port == 443`[cite: 3]
* `icmp`[cite: 3]
* `tcp.flags.syn == 1`[cite: 3]

### What to Look For
* DNS queries[cite: 3]
* HTTP requests[cite: 3]
* TLS handshakes[cite: 3]
* Failed TCP connections[cite: 3]
* ICMP (ping) traffic[cite: 3]
* Large or unusual data transfers[cite: 3]

---

## 3. Basic Log Analysis

### Common Log Sources
* Windows Event Logs[cite: 3]
* Linux Syslog[cite: 3]
* Firewall Logs[cite: 3]
* Web Server Logs[cite: 3]
* IDS/IPS Logs (Snort, Suricata)[cite: 3]
* SIEM Alerts (Wazuh, Splunk)[cite: 3]

### Sample Log
`2026-08-04 10:12:33 LOGIN_FAILED user=admin ip=192.168.1.50`[cite: 3]

### Analyst Triage Questions
* Who attempted the login?[cite: 3]
* From which IP?[cite: 3]
* How many attempts?[cite: 3]
* Is it repeated?[cite: 3]
* Is the IP known or suspicious?[cite: 3]

---

## 4. Understanding System & Network Events

### Normal Events
* Successful login[cite: 3]
* DNS lookup[cite: 3]
* File creation[cite: 3]
* Web browsing[cite: 3]

### Suspicious Events
* Multiple failed logins[cite: 3]
* New administrator account[cite: 3]
* Unusual outbound connections[cite: 3]
* PowerShell or Command Prompt launched unexpectedly[cite: 3]
* Large data uploads[cite: 3]
* Connections to unknown IP addresses[cite: 3]

---

## 5. Practical Exercises

### Exercise 1: Wireshark
1. Start a packet capture[cite: 3].
2. Visit a few websites[cite: 3].
3. Apply these filters:
   * `dns`[cite: 3]
   * `http`[cite: 3]
   * `tcp`[cite: 3]
   * `tls`[cite: 3]
4. Identify:
   * Your DNS queries[cite: 3]
   * Destination IPs[cite: 3]
   * HTTPS traffic[cite: 3]

### Exercise 2: Log Analysis

#### Step 1: Create `sample.log`
Create a file named `sample.log` with the following content[cite: 3]:

* INFO User login successful[cite: 3]
* WARNING Multiple failed login attempts[cite: 3]
* ERROR SQL Injection attempt detected[cite: 3]
* INFO File uploaded[cite: 3]
* WARNING Brute force attack suspected[cite: 3]

#### Step 2: Python Script (`log_analysis.py`)
Write a Python script that reads `sample.log` and prints only the `WARNING` and `ERROR` entries[cite: 3]:

```python
def filter_logs(file_path):
    target_levels = ("WARNING", "ERROR")
    
    try:
        with open(file_path, "r") as file:
            print("--- Filtered Log Entries ---")
            for line in file:
                if any(level in line for level in target_levels):
                    print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")

if __name__ == "__main__":
    filter_logs("sample.log")
