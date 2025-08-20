# Mostramos el menú
print(
    """
    Hola!

    Elige qué operación usar:

    1. Sumar
    2. Restar
    3. Multiplicar
    4. Dividir
    """
)

prompt = "> "

# Pedimos la selección y la convertimos a entero
try:
    seleccion = int(input(prompt))
except ValueError:
    print("Error: Debes ingresar un número válido.")
    exit()

# Verificamos que la opción sea válida y pedimos los números
if seleccion in [1, 2, 3, 4]:
    print("Ahora dime con qué números vas a operar:")
    try:
        num1 = float(input("El primer número: "))
        num2 = float(input("El segundo número: "))
    except ValueError:
        print("Error: Debes ingresar números válidos.")
        exit()

    # Usamos match para elegir la operación
    match seleccion:
        case 1:
            resultado = num1 + num2
            print(f"Resultado: {num1} + {num2} = {resultado}")
        case 2:
            resultado = num1 - num2
            print(f"Resultado: {num1} - {num2} = {resultado}")
        case 3:
            resultado = num1 * num2
            print(f"Resultado: {num1} × {num2} = {resultado}")
        case 4:
            if num2 == 0:
                print("Error: No se puede dividir entre cero.")
            else:
                resultado = num1 / num2
                print(f"Resultado: {num1} ÷ {num2} = {resultado}")
else:
    print("Opción no válida. Elige un número entre 1 y 4.")
