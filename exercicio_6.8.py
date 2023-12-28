#modifique o primeiro exemplo(programa 6.9)de forma a realiza a mesma tarefa, mais sem utiliza a variavel achou.
#Dica: observe a condição de saida do while.
l = [15,7,27,39]
p = int(input("digiti o valor a procurar:"))
achou = False
x = 0
while x< len(l):
    if l[x]== p:
        break
    x+=1
if x != len(l) : 
    print(f"{p}achado na posição{x}")
else: 
    print(f"{p} nao encontrado")        