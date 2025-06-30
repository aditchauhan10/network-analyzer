import sqlite3
import pandas as pd
import numpy as np

# Connect to the SQLite database
conn = sqlite3.connect('network_packets.db')

# Read all packet data into a DataFrame
df = pd.read_sql_query("SELECT * FROM packets", conn)

# Calculate z-score for packet size
df['z_score_size'] = (df['packet_size'] - df['packet_size'].mean()) / df['packet_size'].std()

# Mark packets with a z-score > 2 as anomalies
df['is_anomaly'] = df['z_score_size'].apply(lambda x: abs(x) > 2)

# Display packets considered anomalous by size
print("\n📌 Packet Size Anomalies (Z-Score > 2):")
print(df[df['is_anomaly'] == True][['timestamp', 'src_ip', 'dst_ip', 'packet_size', 'z_score_size']])

# Close DB connection
conn.close()
