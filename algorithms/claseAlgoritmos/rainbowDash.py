skibidiToilet = [4,7,10,13,16,19,22]

def encontrarM(skibidiToilet):
    mayor = skibidiToilet[0]
    for tilina in skibidiToilet:
        if (tilina > mayor):
            mayor = tilina
    return tilina

print(encontrarM(skibidiToilet))