import socket

IP = "127.0.0.1"
PUERTO = 65432

# Crear el socket del cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectarse al servidor
cliente.connect((IP, PUERTO))

# Enviar un mensaje
mensaje = "Hola servidor, soy el cliente"
cliente.sendall(mensaje.encode())

# Recibir la respuesta
respuesta = cliente.recv(1024).decode()

# Mostrar la respuesta
print(f"Respuesta del servidor: {respuesta}")

# Cerrar la conexión
cliente.close()
