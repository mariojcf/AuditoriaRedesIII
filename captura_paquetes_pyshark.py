import pyshark

def capturar_paquetes(interface, cantidad=10):
    print(f"Capturando {cantidad} paquetes en la interfaz: {interface}")
    captura = pyshark.LiveCapture(interface=interface)
    for i, paquete in enumerate(captura.sniff_continuously(packet_count=cantidad)):
        print(f"Paquete {i+1}: {paquete.highest_layer} -> {paquete.summary()}")

if __name__ == "__main__":
    interfaz = input("Introduce la interfaz de red (ej: en0, eth0, Wi-Fi): ")
    cantidad = int(input("Cantidad de paquetes a capturar: "))
    capturar_paquetes(interfaz, cantidad)
