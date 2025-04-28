import socket

def conectar_al_servidor():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_ip = input("Introduce la IP del servidor: ")
    cliente.connect((servidor_ip, 12345))
    mensaje = input("Escribe el mensaje a enviar: ")
    cliente.send(mensaje.encode())
    respuesta = cliente.recv(1024).decode()
    print(f"Servidor responde: {respuesta}")
    cliente.close()

if __name__ == "__main__":
    conectar_al_servidor()
