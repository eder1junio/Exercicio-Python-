#Reescreva o progrma 5.1 de fomra a continua executando ate que o valor digitado seja 0. Utilize repetição aninhada.
import time
while True:
    valor = float(input("digite o valor a paga ou 0  para sair"))
    cedulas = 0
    atual = 100
    apagar = valor 
    if valor ==0:
        print('fim do programa')
        break
    while True:
        if valor <=0.01:
            print("valor muito baixo")
            break
        if atual <= apagar:
            apagar -= atual
            cedulas += 1 

        else: 
            print(f'{cedulas} cedulas(s) de R${atual}')
            if apagar == 0:
                break
            if atual == 100:
                atual = 50
            elif atual == 50:
                atual =20
            elif atual ==20:
                atual =10
            elif atual == 10:
                atual = 5
            elif atual == 5:
                atual = 1
            else:
                if atual == 0.01:
                    break
                elif atual == 1:
                    atual= 0.50
                elif atual == 0.50:
                    atual = 0.10
                elif atual == 0.10:
                    atual = 0.05
                elif atual == 0.05:
                    atual = 0.01
            time.sleep(1)       
            cedulas = 0   