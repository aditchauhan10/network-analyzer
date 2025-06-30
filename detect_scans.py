import sqlite3
import pandas as pd
from ipaddress import ip_network, ip_address

def detect_scans(db_path, cidr_range, threshold=5):
    # Connect to the database and load packet data
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM packets", conn)
    conn.close()

    # Filter only those packets where destination IP is within the provided network (CIDR)
    local_network = ip_network(cidr_range)
    df = df[df['dst_ip'].apply(lambda ip: ip_address(ip) in local_network)]

    # Combine destination IP and port into a single field to count unique scans
    df['dst_combo'] = df['dst_ip'] + ':' + df['dst_port'].astype(str)

    # Group by source IP and count how many unique destination combos each tried to reach
    scan_summary = df.groupby('src_ip')['dst_combo'].nunique().reset_index()
    scan_summary.columns = ['src_ip', 'unique_targets']

    # Select source IPs that have scanned more targets than the threshold
    suspected_scans = scan_summary[scan_summary['unique_targets'] >= threshold]

    return suspected_scans
