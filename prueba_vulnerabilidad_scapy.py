from scapy.all import *

def enviar_paquete_syn(target_ip, target_port):
    print(f"Enviando paquete SYN a {target_ip}:{target_port}")
    ip = IP(dst=target_ip)
    syn = TCP(dport=target_port, flags="S")
    paquete = ip / syn
    respuesta = sr1(paquete, timeout=2, verbose=0)

    if respuesta is None:
        print("No hubo respuesta, puerto filtrado o host no disponible.")
    elif respuesta.haslayer(TCP) and respuesta.getlayer(TCP).flags == 0x12:
        print(f"Puerto {target_port} está ABIERTO.")
        rst = IP(dst=target_ip) / TCP(dport=target_port, flags="R")
        send(rst, verbose=0)
    else:
        print(f"Puerto {target_port} está CERRADO o filtrado.")

if __name__ == "__main__":
    ip = input("Introduce la IP objetivo: ")
    puerto = int(input("Introduce el puerto a evaluar: "))
    enviar_paquete_syn(ip, puerto)
