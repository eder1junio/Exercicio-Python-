#usando a função mdc definida no exercicio anterior,defina uma função para calcular o menor multiplo comun (m.m.c)entre dois numero.
def MDC(a,b):
    if b == 0:
        return a
    else: 
        return MDC(b, a%b)
    

def mmc(a, b):
    return abs(a*b)/MDC(a,b)

print(mmc(48,18))    