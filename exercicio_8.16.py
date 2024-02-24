#escreva um generator capaz de gera seguencia de numeros primos.

def ver_primos(n):
    lis = []
    for t in range(1,n+1):
        if n%t == 0:
            lis.append(t)   
            if len(lis)> 2:
                return False
    if len(lis)==2:
        return True

                
def ger_prinos(n):
    for i in range(n):
        if ver_primos(i):
            yield i        

g = ger_prinos(10)

while True:
    sn = input("Vc gostaria de monstra o proximo numero")
    if sn in "nN":
        break
    print(next(g))