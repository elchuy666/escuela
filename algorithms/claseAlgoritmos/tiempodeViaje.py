tiempo = int(input())
lista= [86400, 3600, 60, 1]
times = ["dias", "horas", "minutos", "segundos"]
imprimir =[]
x = 0
for c in lista:
    if tiempo%c > 0:
        imprimir.append(tiempo//c)
        tiempo = tiempo%c
        
    else:
        x+=1
print(imprimir)