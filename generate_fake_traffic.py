from faker import Faker
import sqlite3
import random
import time

# Initialize Faker and database connection
fake = Faker()
conn = sqlite3.connect('network_packets.db')
c = conn.cursor()

# Insert 50 fake TCP packets
for _ in range(50):
    ts = time.strftime('%Y-%m-%d %H:%M:%S')
    src_ip = fake.ipv4()
    dst_ip = fake.ipv4()
    src_port = random.randint(1024, 65535)
    dst_port = random.randint(20, 443)
    size = random.randint(40, 1500)

    c.execute(
        '''INSERT INTO packets 
        (timestamp, src_ip, dst_ip, src_port, dst_port, packet_size) 
        VALUES (?, ?, ?, ?, ?, ?)''',
        (ts, src_ip, dst_ip, src_port, dst_port, size)
    )

conn.commit()
conn.close()

print("✅ Inserted 50 fake packets.")
