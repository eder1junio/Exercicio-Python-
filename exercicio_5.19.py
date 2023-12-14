# Modifique o progrma para aceita valores decimais, ou seja, tambem contas as moedas de 0,01 , 0,05, 0,10, 0,50.,
import time
valor = float(input("digite o valor a paga"))
cedulas = 0
atual = 100
apagar = valor 
while True:
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