#escreva um programa que verifica se e um palindromo. um numero e palindromo se continuaro mesmo caso seus digitos serja invertidos.
while True:
    n = str(input("digite um nimero para verifica se e palidromo"))
    cont = 0
    if n == "0":
        break 
    for n1 in range(0,len(n)):
        if n[0+n1] == n[-1-n1]:
            cont +=1
    if cont == len(n):
        print('E um palidromo') 
    elif cont != len(n) :
        print("nao e um palidromo")  
print('fin do progrma')                        


