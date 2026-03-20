PYTHON

from scapy.all import sniff, IP, TCP, UDP, Raw

def analyze_packet(packet):
    # 1. Check karein agar packet mein IP Layer hai
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        proto = ip_layer.proto # 6 for TCP, 17 for UDP

        print(f"\n[+] IP Packet: {src_ip} -> {dst_ip} | Protocol: {proto}")

        # 2. Agar TCP Protocol hai (Web, SSH, etc.)
        if packet.haslayer(TCP):
            tcp_layer = packet[TCP]
            print(f"    [Type] TCP | Source Port: {tcp_layer.sport} -> Dest Port: {tcp_layer.dport}")
            
            # Payload (Data) check karein
            if packet.haslayer(Raw):
                print(f"    [Payload]: {packet[Raw].load}")

        # 3. Agar UDP Protocol hai (DNS, Streaming, etc.)
        elif packet.haslayer(UDP):
            udp_layer = packet[UDP]
            print(f"    [Type] UDP | Source Port: {udp_layer.sport} -> Dest Port: {udp_layer.dport}")

# Sniffing Start Karein
print("--- Network Sniffer Start Ho Raha Hai ---")
print("Band karne ke liye Ctrl+C dabayein...")

# store=False taaki memory full na ho
# prn=analyze_packet har packet par function ko run karega
sniff(prn=analyze_packet, store=False)
