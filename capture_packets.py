from scapy.all import sniff, IP, TCP
import sqlite3
import time

# Connect to SQLite database (or create one)
conn = sqlite3.connect('network_packets.db')
c = conn.cursor()

# Create table to store packet info
c.execute('''CREATE TABLE IF NOT EXISTS packets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    src_ip TEXT,
    dst_ip TEXT,
    src_port INTEGER,
    dst_port INTEGER,
    packet_size INTEGER
)''')
conn.commit()

# Function to process each packet
def process_packet(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        ts = time.strftime('%Y-%m-%d %H:%M:%S')
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
        size = len(packet)

        # Insert data into database
        c.execute("INSERT INTO packets (timestamp, src_ip, dst_ip, src_port, dst_port, packet_size) VALUES (?, ?, ?, ?, ?, ?)",
                  (ts, src_ip, dst_ip, src_port, dst_port, size))
        conn.commit()

        print(f"Captured: {src_ip}:{src_port} → {dst_ip}:{dst_port} | Size: {size}")

# Start packet sniffing
print("Capturing packets... Press Ctrl+C to stop.")
sniff(filter="tcp", prn=process_packet, count=50)

conn.close()
