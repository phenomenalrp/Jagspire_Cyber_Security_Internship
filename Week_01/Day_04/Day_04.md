# Day 4: Networking, Wireshark & Log Analysis

---

## 1. Basic Networking Concepts

### IP Address
A unique identifier assigned to a device on a network.
* **IPv4:** `192.168.1.10`
* **IPv6:** `2001:db8::1`

### DNS (Domain Name System)
Converts human-readable domain names into IP addresses.
> **Example:** `google.com` $\rightarrow$ `142.250.x.x`

### HTTP vs. HTTPS

| Feature | HTTP | HTTPS |
| :--- | :--- | :--- |
| **Default Port** | 80 | 443 |
| **Encryption** | Unencrypted (Plaintext) | Encrypted (TLS/SSL) |
| **Security Level** | Less Secure | Secure |

### Common Network Ports

| Port | Service / Protocol |
| :--- | :--- |
| **20 / 21** | FTP (File Transfer Protocol) |
| **22** | SSH (Secure Shell) |
| **23** | Telnet |
| **25** | SMTP (Simple Mail Transfer Protocol) |
| **53** | DNS (Domain Name System) |
| **80** | HTTP (Hypertext Transfer Protocol) |
| **110** | POP3 (Post Office Protocol v3) |
| **143** | IMAP (Internet Message Access Protocol) |
| **443** | HTTPS (HTTP Secure) |
| **3389** | RDP (Remote Desktop Protocol) |

---

## 2. Wireshark Basics

### What is Wireshark?
A network protocol analyzer used to capture, inspect, and analyze network traffic in real time.

### Common Display Filters
* `ip.addr == 192.168.1.10` — Filters traffic involving a specific IP address
* `http` — Displays HTTP traffic
* `dns` — Displays DNS queries and responses
* `tcp.port == 443` — Filters traffic on TCP port 443 (HTTPS)
* `icmp` — Displays ICMP (ping) traffic
* `tcp.flags.syn == 1` — Captures TCP SYN packets (connection requests)

### Key Artifacts to Inspect
* DNS queries and domain resolution
* Plaintext HTTP requests/responses
* TLS handshake sequences
* Failed TCP connection attempts (e.g., port scans)
* ICMP ping sweeps
* Large or abnormal data transfers (potential data exfiltration)

---

## 3. Basic Log Analysis

### Common Log Sources
* **Windows Event Logs** (Security, System, Application)
* **Linux Syslog** (`/var/log/syslog`, `/var/log/auth.log`)
* **Firewall Logs** (Allowed/Blocked traffic)
* **Web Server Logs** (Apache, Nginx, IIS)
* **IDS/IPS Logs** (Snort, Suricata)
* **SIEM Alerts** (Wazuh, Splunk, Microsoft Sentinel)

### Sample Log Entry
```text
2026-08-04 10:12:33 LOGIN_FAILED user=admin ip=192.168.1.50
