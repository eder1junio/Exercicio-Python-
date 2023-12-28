#modifique o programa 6.6 usando o for. Explique por que nem todo os while podem ser transformado em for. 
l = []
while True:
    n = int(input('digite um numero (0 sai):'))
    if n == 0:
        break
    l.append(n)
x = 0
while x< len(l):
    print(l[x])
    x+=1