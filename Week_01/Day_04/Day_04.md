Day 4 

1. Basic Networking Concepts
IP Address
A unique identifier assigned to a device on a network.
IPv4: 192.168.1.10
IPv6: 2001:db8::1

DNS (Domain Name System)
Converts domain names into IP addresses.
Example:
google.com → 142.250.x.x

HTTP vs HTTPS
HTTP HTTPS
Port 80 Port 443
Unencrypted Encrypted (TLS/SSL)
Less secure Secure

Common Ports
Port Service
20/21 FTP
22 SSH
23 Telnet
25 SMTP
53 DNS
80 HTTP
110 POP3
143 IMAP
443 HTTPS
3389 RDP


2. Wireshark Basics
What is Wireshark?
A network protocol analyzer used to capture and inspect network traffic.
Common Display Filters
ip.addr == 192.168.1.10
http
dns
tcp.port == 443
icmp
tcp.flags.syn == 1
What to Look For
DNS queries
HTTP requests
TLS handshakes
Failed TCP connections
ICMP (ping) traffic
Large or unusual data transfers


3. Basic Log Analysis
Common Log Sources
Windows Event Logs
Linux Syslog
Firewall Logs
Web Server Logs
IDS/IPS Logs (Snort, Suricata)
SIEM Alerts (Wazuh, Splunk)
Sample Log
2026-08-04 10:12:33 LOGIN_FAILED user=admin ip=192.168.1.50
Questions to ask:
Who attempted the login?
From which IP?
How many attempts?
Is it repeated?
Is the IP known or suspicious?


4. Understanding System & Network Events
Normal Events
Successful login
DNS lookup
File creation
Web browsing
Suspicious Events
Multiple failed logins
New administrator account
Unusual outbound connections
PowerShell or Command Prompt launched unexpectedly
Large data uploads
Connections to unknown IP addresses
Practical Exercises
Exercise 1: Wireshark
Start a packet capture.
Visit a few websites.
Apply these filters:
dns
http
tcp
tls
Identify:
Your DNS queries
Destination IPs
HTTPS traffic

Exercise 2: Log Analysis
Create a file called sample.log:
INFO User login successful
WARNING Multiple failed login attempts
ERROR SQL Injection attempt detected
INFO File uploaded
WARNING Brute force attack suspected
Write a Python script that prints only the WARNING and ERROR entries.