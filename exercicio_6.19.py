#escreva um programa que compare duas lista. Utilizando operaçoes com conjuntos,imprima:
#1º os valores comun a duas lista
#2º os valores que existe so na primeira 
#3ºos valores que exite a so na segunda 
#4ºuma lista com os elementos nao repetidos na duas lista.
#5º a primeira lista sem os elementos repetidos na segunda.

list1 = [1,5,3,4,8] 
list2 = [4,5,9,7,1,]
conjunto = set(list1)
conjunto1 = set(list2)
uniao = conjunto| conjunto1
print(uniao)
intercecao = conjunto & conjunto1
print(intercecao)
conjun2 = conjunto - conjunto1
print(conjun2)

conjun2 = conjunto1 - conjunto
print(conjun2)
print("Uma lista com os elementos nao repetidos na duas lista.")
naorep =list (conjunto.union(conjunto1))
print(naorep)