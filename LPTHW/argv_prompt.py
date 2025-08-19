from sys import argv

script, user_name = argv
prompt = "> "

print(f"Hola {user_name}, im the {script} script.")
print("Tu me das like?")
likes = input(prompt)

print(f"Donde vives? {user_name}")
lives = input(prompt)

print("Que ordenador tienes?")
computer = input(prompt)

print(
    f"""
       El diablo asaroso, entonces dices que me {likes} das like.
       Vives en {lives}. Mu chulo.
       Y tienes un {computer} de ordenador.
       """
)

