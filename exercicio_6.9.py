#Modifique o exemplo para pesquisa dois valores.em vez de apena p. leia outro valor v que tambem sera procurado. na impressao 
#indique qual valor foi achado primeiro.

l = [15,7,27,39]

p = int(input("digiti o valor a procurar:"))
v = int(input("digite outro valor a ser prcurado:"))
x= 0 
achou = [False,False]
while x< len(l):
    
    if l[x]== p:
        print(f"{p}achado na posição{x}")
        achou[0] = True 
    elif l[x] == v:
        print(f"{v}achado na posição{x}")
        achou[1] = True
    x+=1 
    if achou[0] and achou[1]:
        break
if achou[0] == False:
    print(f'{p} nao encontrador')
if achou[1] == False:
        print(f'{v} nao encontrador')


         