#Define uma função recursica que calcule o maior divisor comum(m.d.c)entre numeros a e b em que a>b.

def MDC(a,b):
    if b == 0:
        return a
    else: 
        return MDC(b, a%b)
    

print(MDC(48,18))
