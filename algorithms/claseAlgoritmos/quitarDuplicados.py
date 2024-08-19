cadena = input()
separado = cadena.split(", ")
repetidos = ", ".join(dict.fromkeys(separado))

print(repetidos)