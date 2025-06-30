# Network Packet Analyzer & Anomaly Detector

This project is a complete Python-based tool to monitor, analyze, and detect anomalies in TCP traffic over your local WiFi network. It uses Scapy for packet capture and Streamlit to visualize and interact with the data.


## Features

- Live TCP Packet Capture using Scapy  
- Anomaly Detection using Z-Score (for packet size)  
- Port Scan Detection via IP to multiple IP:Port fan-out logic  
- SQLite Database Storage for persistence  
- Streamlit Dashboard to view:
  - Raw packets  
  - Anomalies  
  - Scan attempts  
  - Charts for packet size and top talkers  
- Fake Data Generator for testing (uses faker)


## Folder Structure
network-analyzer/
├── app.py # Streamlit web dashboard
├── capture_packets.py # Capture live network packets
├── generate_fake_traffic.py # Generate test packets
├── anomaly_detection.py # Z-score based anomaly detection
├── ip_statistics.py # Summarizes IP stats
├── detect_scans.py # Detects port scan patterns
├── network_packets.db # SQLite DB (auto-created)

## Requirements

Install all dependencies using pip:

```bash
pip install scapy pandas numpy faker streamlit plotly ipaddress


How to Run:-
1)Capture real packets (requires admin/root permission):
python capture_packets.py

2)Generate fake packets (optional for testing):
python generate_fake_traffic.py

3)Launch Streamlit dashboard:
streamlit run app.py


Learnings:-

TCP/IP Packet Structure
Packet sniffing with Scapy
Z-Score Anomaly Detection
IP fan-out pattern-based scan detection
Streamlit dashboard design
SQLite integration with live network data

Disclaimer:-
This tool is meant strictly for educational and local testing purposes.
Do not use it on networks without permission.
