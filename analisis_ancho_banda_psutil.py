import psutil
import time

def medir_trafico(intervalo=1, duracion=10):
    print(f"Monitoreando tráfico durante {duracion} segundos...\n")
    inicio = psutil.net_io_counters()
    time.sleep(intervalo)
    for _ in range(int(duracion / intervalo)):
        actual = psutil.net_io_counters()
        bytes_enviados = (actual.bytes_sent - inicio.bytes_sent) / intervalo
        bytes_recibidos = (actual.bytes_recv - inicio.bytes_recv) / intervalo
        print(f"Velocidad - Enviado: {bytes_enviados / 1024:.2f} KB/s | Recibido: {bytes_recibidos / 1024:.2f} KB/s")
        inicio = actual
        time.sleep(intervalo)

if __name__ == "__main__":
    duracion = int(input("Introduce duración total en segundos: "))
    medir_trafico(1, duracion)
