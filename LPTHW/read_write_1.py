from sys import argv

script, filename = argv

print(f"Vamos a borrar {filename}")
print("Si NO quieres, pulsa CTRL-C (^C).")
print("Si quieres continuar, pusla ENTER")

input("?")

print("Abriendo...")
target = open(filename, "w")

print("Truncando el archivo. Diablura")
# target.truncate() // al usar 'w' no hace falta, ya elimina todo lo que habia antes.

print("Ahora te pregunto por 3 lineas.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("Escribiendo...")

target.write(line1)
target.write("\n")

target.write(line2)
target.write("\n")

target.write(line3)
target.write("\n")

print("Ahora lo cerramos.")
target.close()
