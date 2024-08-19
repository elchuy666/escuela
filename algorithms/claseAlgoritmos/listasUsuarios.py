'''se debe de dar una cadena de texto y el programa la debe de volver un array'''

a = input("escribe arreglos de numeros separados por un gato, y espacios").split("#")

print(a)
b =[]
for i in range(len(a)):
    b.append(a[i].split())

print(b)