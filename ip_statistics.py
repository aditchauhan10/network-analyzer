import sqlite3
import pandas as pd

# Connect to the database and load data
conn = sqlite3.connect('network_packets.db')
df = pd.read_sql_query("SELECT * FROM packets", conn)

# Top IPs by number of packets sent
print("\n Top IPs Sending the Most Packets:")
print(df['src_ip'].value_counts().head(5))

# IPs sending the most total data
print("\n IPs Sending Most Data (Total Packet Size):")
print(df.groupby('src_ip')['packet_size'].sum().sort_values(ascending=False).head(5))

# Most common IP:Port combinations
print("\n Most Frequent IP:Port Combinations:")
df['ip_port'] = df['src_ip'] + ':' + df['src_port'].astype(str)
print(df['ip_port'].value_counts().head(5))

# Close the database connection
conn.close()
