def find (cad, c, pos):
    while pos < len(cad):
        if c == cad[pos]:
            return pos
        pos += 1
    return -1
#print(find("Adirana", "i", 5))

def find2 (cad, c, pos):
             for x in range(pos, len(cad)):
                  if c == cad[x]:
                       return x
             return -1
#print(find("Totoro", "o", 2))

def count(cad, c):
      contador = 0
      for x in cad:
            if c == x:
                  contador +=1
      return contador
#print(count)

def isLower (c):
      if "a" <= c <= "z":
            return True
      else:
            return False
      
#print(isLower("A"))

def todasMinusculas (cad):
      for x in cad:
            if not (isLower(x)):
                  return False
      return True

print(todasMinusculas("adrOan"))