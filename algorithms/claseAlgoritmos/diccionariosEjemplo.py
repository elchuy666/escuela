diccionario = {".,?!:":1,"abc":2,"def":3,"ghi":4,"jkl":5,"mno":6,"pqr":7,"tuv":8,"wxyz":9," ":0}
frase = input("dame la frase perro. ")

def numerosMarcados(frase):
    for i in frase:
        for x in diccionario:
            