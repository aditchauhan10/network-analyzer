import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import plotly.express as px
from detect_scans import detect_scans

DB_PATH = "network_packets.db"

# App title
st.title("Network Packet Analyzer and Scan Detector")

# Load packet data from SQLite database
conn = sqlite3.connect(DB_PATH)
df = pd.read_sql_query("SELECT * FROM packets", conn)
conn.close()

# Sidebar filters
st.sidebar.header("Filter Settings")
cidr_range = st.sidebar.text_input("Enter your network CIDR (e.g., 192.168.1.0/24):", "192.168.1.0/24")
size_threshold = st.sidebar.slider("Anomaly Z-Score Threshold", min_value=1.0, max_value=5.0, value=2.0)
scan_threshold = st.sidebar.slider("Scan Detection Threshold (unique targets)", 3, 30, 5)

# Show raw data option
if st.checkbox("Show raw packet data"):
    st.dataframe(df)

# Anomaly detection using Z-score
df['z_score'] = (df['packet_size'] - df['packet_size'].mean()) / df['packet_size'].std()
df['is_anomaly'] = df['z_score'].abs() > size_threshold
anomalies = df[df['is_anomaly']]

# Display anomaly results
st.subheader("Detected Packet Size Anomalies")
st.write(anomalies[['timestamp', 'src_ip', 'dst_ip', 'packet_size', 'z_score']])

# Histogram of packet sizes
st.subheader("Packet Size Distribution")
fig = px.histogram(df, x="packet_size", nbins=30)
st.plotly_chart(fig)

# Scan detection logic
st.subheader("Potential Network Scans")
scan_sources = detect_scans(DB_PATH, cidr_range, threshold=scan_threshold)
st.write(scan_sources)

# Top IPs sending highest traffic
st.subheader("Top Source IPs by Total Data Sent")
top_talkers = df.groupby('src_ip')['packet_size'].sum().sort_values(ascending=False).head(5)
st.bar_chart(top_talkers)

# Footer
st.markdown("---")
st.markdown("Developed by Adit")
