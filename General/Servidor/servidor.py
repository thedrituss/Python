import socket

IP = "127.0.0.1"
PUERTO = 65432

# Crear el socket
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincular el socket a la IP y puerto (127.0.0.1:65512)
servidor.bind((IP, PUERTO))

# Servidor a escuchar
servidor.listen()

print(f"Servidor escuchando en {IP}:{PUERTO}...")
conexion, direccion = servidor.accept()

# Recibir el mensaje del cliente
mensaje = conexion.recv(1024).decode()

print(f"Mensaje del cliente {direccion}: {mensaje}")

# Enviar respuesta al cliente
respuesta = f"Mensaje recibido: {mensaje}"
conexion.sendall(respuesta.encode())

# Cerrar conexiones
conexion.close()
servidor.close()
