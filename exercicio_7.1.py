#escreva um progrma que leia duas strings.verifica se a segunda ocorre dentro da primeira e imprima a posição de inicio.
#1ª string AABBEFAATT 2ª STRING BE Resultado BE encontra na posição 3 de aabbefaatt

N = "A MARIA BEIJOU O JOAO "
nome = "BEIJOU"

pos = N.find(nome)

print(f"{nome} encontrado na posição {pos} de {N}")