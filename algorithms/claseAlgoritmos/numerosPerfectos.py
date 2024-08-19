n = int(input())
s = 0
x = 1
while not x == n:
    if n%x == 0:
        s+=x
    x+=1
def checarNumero(s, n):
    return s == n
print(checarNumero(s, n))