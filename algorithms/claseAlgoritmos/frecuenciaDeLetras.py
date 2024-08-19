cadena = input()
lista1 =[tuple( x, cadena.count(x)) for x in cadena]
print(lista1)