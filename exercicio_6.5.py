# altere o programa 6.7 de forma atrabalha com varios comandos digitados de uma so vez.atualmento so um comando pode ser inserido por vez
#altere-o de forma a considera operação como uma strig.
ultimo = 10
fila =list(range(1,ultimo+1))
list = []
while True:
    while True:
        print(f'\nExistem{len(fila)} cliente na fila')
        print(f'fila atual:{fila}')
        print('Digite F para adiciona um cliente ao fim da fila,')
        print(' ou A para realiza o atendimentos, s para sair')
        operacao = input('operação(f,a,s)')
        list.append(operacao)
        if operacao == "s":
             print(list)
             break
    for t in list:        
        if t == "a":
            if len(fila) >0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print("fila vazia: Ninguem para atender")
        elif t == "f":
            #quat = int(input("voce gostaria de adiciona quantas pessoas"))
            #for r in range(1,quat+1):
                ultimo +=1 
                fila.append(ultimo) 
        elif t == "s":
            break
        else:
            print("operação invalida!Digite apenas f,a ou s")
    print(fila)        
    break        