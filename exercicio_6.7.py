#Faça um progrma que leia uma expreção com parênteses. usando pilhas, verifique se o parenteses foram abertos e fechados nna
#ordem correta. exemplos (()) ok , ()()(()()) ok, (() erro. Voce pode adiciona elementos a pilha sempre que encontra abre parenteses
#e desenpilha - loa cada fechada parenteses. ao desenpilha,verifique se o topo da PILHA E UM ABRE PARENTESES, se a expreção estiver correta
#sua pilha estara vazia no final .

n = input('digite um expressao')
x = 0
cont = 0
while True:
    if n[x] == "(":
        cont+=1
    elif n[x] ==")":
        cont-=1
    x+=1
    if x == len(n):
        break  
   
if cont == 0:
    print('a expreção esta correta' )    
