import requests  # funciona

# Pedir URL al usuario
url = input("Introduce la URL (incluyendo https://): ").strip()

# Hacer la petición
try:
    respuesta = requests.get(url, timeout=10)
except requests.exceptions.RequestException as e:
    print(f"Error al conectar con la URL: {e}")
    exit()

# Obtener cabeceras
cabeceras = respuesta.headers

# Mostrar cabeceras
print("\n=== CABECERAS RECIBIDAS ===")
for clave, valor in cabeceras.items():
    print(f"{clave}: {valor}")

# Análisis de seguridad
print("\n=== ANÁLISIS DE SEGURIDAD ===")

cabeceras_seguridad = {
    "X-Content-Type-Options": "Recomendado: 'nosniff'",
    "X-Frame-Options": "Recomendado: 'DENY' o 'SAMEORIGIN'",
    "X-XSS-Protection": "Recomendado: '1; mode=block'",
    "Strict-Transport-Security": "Recomendado: 'max-age=...' (HSTS)",
    "Content-Security-Policy": "Recomendado: definida según necesidades",
    "Referrer-Policy": "Recomendado: 'no-referrer', 'strict-origin', etc.",
}

for cabecera, recomendacion in cabeceras_seguridad.items():
    if cabecera in cabeceras:
        print(f"✅ {cabecera}: {cabeceras[cabecera]}")
    else:
        print(f"❌ Falta: {cabecera} → {recomendacion}")

# Información extra
print(f"\nServidor: {cabeceras.get('Server', 'No especificado')}")
