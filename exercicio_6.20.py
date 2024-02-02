#escreva um programa que compare duas lista. Considera a primeira lista como versão inicial e a segunda a versão pos alteração.
#utilizando operações com conjunto seu programa deve imprimi a lista de modificações entre esses duas versão, listado:
#os elementos que nao mudaram, os novo elementos, os elementos que foram removidos 

l = {2,5,8,9,12,6}
l2 = {4,5,7,23,13,3}
# os elemnetos que nao mudaram
lm = l& l2
print(lm)
# os novo elementos
ln = l -l2
print(ln)
#s elementos que foram removidos