dinero = int(input())
total = int(input())
monedas = [10,5,2,1]
cambio = dinero - total
lista = []

for x in range(len(monedas)):
    lista.append(cambio//monedas[x])
    cambio = cambio - lista[x]*monedas[x]

for x in range(len(lista)):
        print(str(lista[x]) + " - $" + str(monedas[x]))