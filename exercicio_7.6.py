#escreva um programa que leia treis string. imprima o resultado da substituição da primeira, dos caracteres da segunda pela terceira.
#1ª string: aattcgaa 2º string: tg 3º string ac resultado aaaaccaa

n = list(input("digite uma frase"))
n1 = input("quais letras vc gostria substituir ")
n2 = input("quais letas vai no lugar ")
cont = 0
cont1 = 0
while True:
    cont1 = 0
    while True:
        if n1[cont] == n[cont1]:
            n[cont1]=n2[cont]
        cont1+=1  
         
        if cont1 == len(n):
            break
        
    cont+=1     
    if cont == len(n1):
        break  
n5 = "".join(n)          
print(n5)   