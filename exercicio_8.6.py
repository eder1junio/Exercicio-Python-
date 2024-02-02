#Reescreva o progrma 8.2 de forma a ultilizar o for em vez de while.

def soma(l):
    soma = 0
    for n in l:
        soma += n
    return soma

l = [4,10,8,20]  

print(soma(l))

#Progrma 8.2 - como nao escreve uma função

def soma(l):
    total = 0
    x = 0
    while x<5:
        total +=l[x]
        x+=1
    return total    