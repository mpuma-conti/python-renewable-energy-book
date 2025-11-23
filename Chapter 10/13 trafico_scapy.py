from scapy.all import sniff
from collections import Counter

# Contador para rastrear IPs
ip_counter = Counter()

def packet_callback(packet):
    if packet.haslayer("IP"):
        src_ip = packet["IP"].src
        ip_counter[src_ip] += 1
        # Si una IP realiza más de 100 solicitudes, se genera una alerta
        if ip_counter[src_ip] > 100:
            print(f"ALERTA: Posible ataque DDoS desde {src_ip}")

# Capturar paquetes en la red
print("Monitoreando tráfico de red...")
sniff(prn=packet_callback, count=0)