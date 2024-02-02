#escreva uma função que escreva o maior de dois numeros: valores esperados maximo(5,6) == 6 maximo(2,1)==2, maximo(7,7) == 7
def maximo(n1,n2):
    if n1 > n2:
        return n1
    if n2>n1:
        return n2
    if n2 == n1:
        return "são iguais "
n1 = int(input("digite um numero "))
n2 = int(input("digite outro numero"))    
    

resp = maximo(n1,n2)  
print(resp) 