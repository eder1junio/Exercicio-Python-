#escreva um progrma que pergunte o depósito inicial e a taxa de juros de uma poupança.  exiba os valores mês a mês para os 24 primeiro
#meses. Escreva o total ganho com o juros no periodo.

valor = float(input('qual o valor do deposito'))
taxa = float(input('qual e a taxa mensal do deposito'))

for n in range(1,25):
    valor = valor+(valor *(taxa/100))
    print(f'mês {n} valor {valor:.2f}')