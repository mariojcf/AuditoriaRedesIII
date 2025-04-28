import socket

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(('0.0.0.0', 12345))
    servidor.listen(5)
    print("Servidor listo y escuchando en el puerto 12345...")

    while True:
        cliente, direccion = servidor.accept()
        print(f"Conexión establecida desde {direccion}")
        mensaje = cliente.recv(1024).decode()
        print(f"Cliente dice: {mensaje}")
        respuesta = "Mensaje recibido correctamente."
        cliente.send(respuesta.encode())
        cliente.close()

if __name__ == "__main__":
    iniciar_servidor()
