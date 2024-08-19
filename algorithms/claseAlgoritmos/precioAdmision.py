visitantes= int(input())
edades=[int(input()) for x in range(visitantes)]
total = 0.0

for x in edades:
    if 12<x<=65:
        total+=230.99
    elif x>65:
        total+=180.30
    elif 3<=x<=12:
        total+=140.50
    else:
        continue
    print(total)