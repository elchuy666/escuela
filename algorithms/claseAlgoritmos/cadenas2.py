'''lista = [1,2,3,4]
i=0

while i < len(lista):
    print(lista[i])
    i += 1

for x in range(len(lista)):
    print(lista[x])'''

'''print("los vectores tienen compnentes x y z")

x = []
y = []

def agruegarXY():
    cantidadDeVectores = int(input("Cuantos vectores quieres sumar?"))
    i = 0
    while i < cantidadDeVectores:
        numeroDeVector=1
        print("vector",numeroDeVector)
        datoX = int(input("dame el componente x"))
        x.append(datoX)
        datoY = int(input("dame el componente y"))
        y.append(datoY)
        numeroDeVector +=1
        i +=1

def sumarVectores(a ,b):
    suma = []
    for x in range(len(a)):
        suma.append(a[x] + b[x])
        return(suma[x])

agruegarXY()
print(sumarVectores(x,y))'''

b = input("dame la cadena")
a = input("Dame el caracter")

contador = 0

def romperCadena(x, y):
    if x[contador] == y:
        cadenaRota= b.split(a)
        return cadenaRota
    else: print("no esta el caracter en la cadena")
