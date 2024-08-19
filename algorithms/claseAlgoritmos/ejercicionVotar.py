import math
from time import sleep
"""edad=int(input("Que edad tienes?"))
if(edad>17)==True:
    print("si puedes, vota por amlo")
else:
    print("tas chavo ya vete")



promedio = int(input("dime tu promedio."))
semestre = int(input("dime en que semestre vas."))
if(promedio>8.5 and semestre>5):
    print("PUEDES IRTE ALV AL EXTRANJERO!!!!!")
if(promedio>=8 and semestre>5):
    print("puedes aplicar a la beca PAPIIT")
if(promedio>=8 and 2<semestre):
    print("puedes aplicar a la beca PAPIME")
else:
    print("no te alcanza mi chaboot")


#escribir programa que muestre menu
a = int(input("dame el primer numero pero en fa"))
b = int(input("dame el segundo"))

def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def division(a,b):
    return a/b
def modulo(a,b):
    return a%b

operacion = input("dime que operacion quieres perro.\n suma\n resta\n multiplicacion\n division\n modulo\nescribelo todo en minusculas")
if (operacion=="suma"):
    print(suma(a,b))
elif(operacion=="resta"):
    print(resta(a,b))
elif(operacion=="multiplicacion"):
    print(multiplicacion(a,b))
elif(operacion=="division"):
    print(division(a,b))
elif(operacion=="modulo"):
    modulo(a,b)
else:
    print("no me diste nada para chambear")


#ejercicio cafeteria.
categoria = input("pon tu categoria")
consumo = float(input("Coste consumo"))
retardos = int(input("Numero de retardos"))

if categoria == "A":
    total=consumo*.9
elif categoria == "B":
    total=consumo*.8
elif categoria == "C":
    total=consumo*.7
else:
    print("No xexiste categoria")


if retardos<= 3:
    total = total*.9
print("El costo final es: ", total)"""

#Ejercicio areas
"""def menu():
    print("Este es el menu de figuras\n1. circulo\n2. rectangulo\n3. triangulo.")
menu()
operacionFiguras = input("Dime la figura de la que quieres calcular el area:")

if(operacionFiguras == "circulo"):
    radio = float(input("dime el radio:"))
    print("el area del circulo es :",math.pi*(radio**2))

elif(operacionFiguras =="rectangulo"):
    altura = float(input("dame la altura:"))
    base = float(input("dame la base:"))
    print("el area del rectangulo es :", base*altura)
elif(operacionFiguras=="triangulo"):
    altura = float(input("dame la altura:"))
    base = float(input("dame la base:"))
    print("El area del trangulo es :", (base*altura)/2)
else:
    print("No conozco esa figura geometrica.")"""

#Ciclos
"""def cuentaRegresiva(n):
    delay = 1
    while n>0:
        print(n)
        sleep(delay)
        n = n-1
    print("Empezamos")

cuentaRegresiva(20)"""

a = int(input("numero"))
b = int(input("numero"))
def multiplos(a,b):
    c = 1
    while (a*c)<b:
        print(a*c)
        c+=1
if (b>a):
    multiplos(a,b)
else:
    print("b es mayor")

#logaritmos
base = float(input("numero base: "))
fila = float(input("numero fila: "))
n = 1

while n <= fila:
    print(n,"   " ,math.log(n, base))
    n +=1

#piramides 

base = int(input("numero de pisos de la piramide: "))
n = 1
while n <= base:
    print(n*"*")
    n +=1

#