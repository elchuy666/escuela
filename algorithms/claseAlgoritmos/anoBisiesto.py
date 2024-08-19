anio = int(input())

def checarBisiesto(anio):
    if anio%4 ==0 and anio%100==0:
        return False
    else:
        return True
    
if checarBisiesto(anio)==False and anio%400 ==0:
    print(True)
else:
    print(False)