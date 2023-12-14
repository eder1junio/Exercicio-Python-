#escreva um progrma que exiba uma lista de opção(menu):adção,subtração,divisão,multiplicação e sair.
#Imprima a tabuada da operação escolhida.Repita ate a opção saida seja escolhida.


while True:
    opcao = int(input("""escolha 1 para adição 
escolha 2 para subtração 
escolha 3 para divisão 
escolha 4 para multiplicação
escolha 5 para sair"""))
    if opcao==1:
        n =int(input('qual numero vc gostaria a tabuada '))
        for n1 in range(1,10):
            print(f'{n1}+{n}={n1+n}')
    elif opcao == 2:
        n =int(input('qual numero vc gostaria a tabuada '))
        for n1 in range(1,10):
            print(f"{n1}-{n}={n-n1}")
    elif opcao == 3:
        n =int(input('qual numero vc gostaria a tabuada '))
        for n1 in range(1,10):
            print(f"{n1}/{n}={n1/n}")
    elif opcao == 4:
        n =int(input('qual numero vc gostaria a tabuada '))
        for n1 in range(1,10):
            print(f"{n1}*{n}={n1*n}")
    elif opcao == 5:
        break
    else:
        print('Digite um opçao valida ')                              
