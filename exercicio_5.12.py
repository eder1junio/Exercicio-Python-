#alteri o progrma anterios de forma a pergunta tambem o valor depositado mensalmente. esse valor sera depositado no incio de cada mês,
# e voce deve considera-lo para cálculo do juros do mes seginte.
depos = float(input("qual o valor do depositl inicial ?"))
deposMen = float(input("qual o valor do deposito mensal ?"))
taxa = float(input('qual a taxa mensal paga ' ))
for n in range(1,25):
    depos = depos   +  depos *taxa/100 
    if n != 1:
        depos+=deposMen
    print(f'mês {n} valor {depos:.2f}')