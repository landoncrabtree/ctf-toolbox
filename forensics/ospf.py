import hashlib
from scapy.all import *

def calculate_md5(packet_data, password):
    # Pad or truncate the password to 16 bytes
    password = password[:16].ljust(16, b'\x00')
    
    # Set last 16 bytes of the packet_data to password
    packet_data = packet_data[:-16] + password

    # Calculate MD5 hash
    md5_hash = hashlib.md5(packet_data).digest()

    return md5_hash

packets = rdpcap('ospf_parsed.pcapng')

# example to crack in-house
for packet in packets:
    ospf_data = packet[Raw].load
    original_hash = ospf_data[-16:]
    candidate = b'password'
    if calculate_md5(ospf_data, candidate) == original_hash:
        print("Password found:", candidate)

# output in john format
for packet in packets:
    ospf_data = packet[Raw].load
    original_hash = ospf_data[-16:]
    ospf_data = ospf_data[:-16]
    print("$netmd5$"+ospf_data.hex()+"$"+original_hash.hex())
