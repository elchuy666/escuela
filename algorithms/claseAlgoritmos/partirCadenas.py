import re

cadena = input()

lista = re.findall('[a-zA-Z][^A-Z]*', cadena)

print(lista)