#escreva um progrma que leia um numero e verifique se e ou nao um numero primo.Para fazer essa verificação, calcule o resto da divisao
#do numeros por 2 depois todos numero impares ate o numeor lido. Se o resto de uma dessa divisão for igual a zero, o numeor nao e primo
#observe oque 0 e 1 nao sao primos e que 2 e o unico numero primo que é par.

n = int(input("digite um numero para verifica que e Primo"))
cont = 0
for n1 in range(1,n):
    if n1!= 1:
        if n%n1 == 0:
            print('nao e primo')
            break
        if n%n1 !=0:
            cont-= 1
if cont<0:
    print('o numero digitado e primo')        



     
       
        
