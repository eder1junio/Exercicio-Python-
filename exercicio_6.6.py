#modifique o programa para trabalha com duas filas. para facilitar seu trabalho, considere o comando a para atendimento na fila 1;
#e b para atendiemento na fila 2. o mesmo para a chegada do clientes: f para fila 1;e g para fila 2.
ultimo = 10
ultimo1 = 10
fila =list(range(1,ultimo+1))
fila1 =list(range(1,ultimo+1))
list = []
while True:
    while True:
        print(f'\nExistem{len(fila)} cliente na fila')
        print(f'fila atual:{fila}')
        print('Digite F para adiciona um cliente ao fim da fila,')
        print(' ou A para realiza o atendimentos, s para sair')
        operacao = input('operação para primeira fila (f,a,),para segunda fila(b,g) para sair s')
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
            ultimo +=1 
            fila.append(ultimo)
            print("adicionado um novo cliente na fila") 
        elif t == "b":
            if len(fila1) >0:
                atendido = fila1.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print("fila vazia: Ninguem para atender")
        elif t == "g":
            ultimo1 +=1 
            fila1.append(ultimo)
            print("adicionado um novo cliente na fila")    
        else:
            print("operação invalida!Digite apenas f,a ou s")
    print(fila,fila1)        
    break        