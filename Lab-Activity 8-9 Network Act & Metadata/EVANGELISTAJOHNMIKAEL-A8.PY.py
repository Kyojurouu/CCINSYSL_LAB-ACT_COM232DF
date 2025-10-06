SUSPICIOUS_THRESHOLD = 20

simulated_packets = [
    ("192.168.1.10", "192.168.1.1", "HTTP"),
    ("192.168.1.20", "192.168.1.1", "HTTPS"),
    ("192.168.1.150", "192.168.1.1", "HTTP"),
    ("192.168.1.10", "192.168.1.2", "FTP"),
    ("192.168.1.150", "192.168.1.3", "HTTPS"),
    ("192.168.1.10", "192.168.1.1", "HTTP"),
    ("192.168.1.150", "192.168.1.5", "HTTP"),
    ("192.168.1.20", "192.168.1.2", "SSH"),
    ("192.168.1.10", "192.168.1.4", "HTTP"),
    ("192.168.1.150", "192.168.1.7", "HTTP"),
    ("192.168.1.10", "192.168.1.1", "HTTP"),
    ("192.168.1.150", "192.168.1.8", "HTTPS"),
    ("192.168.1.10", "192.168.1.1", "HTTP"),
    ("192.168.1.150", "192.168.1.9", "HTTP"),
    ("192.168.1.10", "192.168.1.1", "HTTP"),
    ("192.168.1.150", "192.168.1.10", "HTTPS"),
    ("192.168.1.10", "192.168.1.1", "HTTP"),
    ("192.168.1.150", "192.168.1.11", "HTTP"),
    ("192.168.1.150", "192.168.1.12", "HTTPS"),
    ("192.168.1.150", "192.168.1.13", "HTTP"),
] * 2

def analyze_packets(packets):
    print("Analyzing simulated network packets...")

    packet_counts = {}
    for src, dest, proto in packets:
        packet_counts[src] = packet_counts.get(src, 0) + 1

    print("\nPacket counts per source IP:")
    for ip, count in sorted(packet_counts.items()):
        print(f" - {ip}: {count} packets")

    print("\nChecking for suspicious activity...")
    for ip, count in packet_counts.items():
        if count > SUSPICIOUS_THRESHOLD:
            print(f"!!! ALERT: Suspicious activity detected from {ip}. Packets sent: {count}")

if __name__ == "__main__":
    analyze_packets(simulated_packets)
