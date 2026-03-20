# 🚀 Python Packet Sniffer & IP Intelligence

A network security tool built with **Python** and **Scapy** to capture and analyze live traffic on Kali Linux. It features integrated **WHOIS lookups** to perform real-time OSINT on captured IP addresses.

##  Features
- **Live Sniffing:** Captures IP packets, TCP/UDP protocols, and raw payloads.
- **IP Intelligence:** Identifies the organization behind any captured IP (e.g., Fastly, Google).
- **Clean Output:** Formatted terminal display for easy network monitoring.

## 📸 Proof of Concept

### 1. Packet Capture in Action
Captured packets showing source/destination IPs and protocols:
![Sniffer Output](Python-Packet-Sniffer.py.pdf) 
*(Note: Agar tumne screenshot ko image format mein dala hai, toh uske naam se replace kar dena)*

### 2. Network Analysis (WHOIS)
Identifying the owner of the captured traffic:
![WHOIS Info](assets/your_whois_image_name.png)

## 🛠️ Installation & Usage
1. Clone the repo: `git clone <your-repo-link>`
2. Run with sudo: `sudo python3 mysniffer.py`
