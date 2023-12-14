#modifique o programa anterior de forma a ler um numero n imprima os n primeiro numero primo .

n = 0
cont2 = 0
num = int(input("quantos numero primos vc gostaria ?"))
while cont2 <= num:
    cont = 0
    n+=1
    for n2 in range(1,n+1):
        if n%n2==0:
            cont +=1
    if cont == 2:
        print(f"{n2}e um numero primno")
        cont2 +=1

        

