from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copiando desde {from_file} a {to_file}")

with open(from_file) as in_file:
    indata = in_file.read()

print(f"The input is {len(indata)} bytes long.")

print(f"Does the output file exist? {exists(to_file)}")
print("ENTER para continuar, CTRL-C para abortar")
input()

with open(to_file, "w") as out_file:
    out_file.write(indata)
