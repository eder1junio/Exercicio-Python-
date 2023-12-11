#escreva um progrma para controla uma pequena maquina registradora.
#voce deve solicita ao usuario  que digite o codigo do produto e a quantidade 
#comprada.utileze a tabela do codigoa seguir para obter o preço de cada produto.
#codigo 1 = 0.50, 2 = 1.00, 3=4.00,5=7.00, 9=8.00
#seu programa deve exibi ototal das compras depois que o usuario digita 0.
#qualquer outro codigo deve gera a mensagem de erro "codigo invalido
total = 0 
while True:
    n = int(input('qual o codigo do produto'))
    if n == 1:
        com = int(input('qual a quantidade comprada '))
        total = com * 0.50
    elif n ==2 :
        com = int(input('qual a quantidade comprada '))
        total = com*1
    elif n ==3:
        com = int(input('qual a quantidade comprada '))
        total = com*4
    elif n == 5:
        com = int(input('qual a quantidade comprada '))
        total = com*7
    elif n == 9:
        com = int(input('qual a quantidade comprada '))
        total = com*8  
    elif n == 0:
        break
    else:
        print("opcao invalida,")

print(f"total compro foi de {total}")

