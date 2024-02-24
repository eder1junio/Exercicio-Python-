#Utilizando a função type, escreva uma função recursiva que imprima os elementos
#de uma lista. cada elemento deve ser impresso separadamente. um por linha
#considere o caso da lista dentro de lista como l = [1,[2,3,4,[5,6,7]]].
#a cada nivel, imprima a lista mais a direita. como fazemos a indentar bloco
#em python;dica:envie o nivel atualcomo parametros e utilize para cqalcvular 
#quantidaDE DE ESPAÇos em branco a esquerda de cada elementio.

def imprima(a,r=0):
    for t in a:
        if type(t) == list:
            r+=1
            imprima(t,r)
        else :
            print(f'{" "*r}{t}')

b=[1,[2,3,4,[5,6,7]]]
imprima(b)