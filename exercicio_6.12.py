#altere o Programa 6.11 de forma a imprimir o menor elemento da lisata.
l = [1,7,2,4]
maximo = l[0]
for e in l:
    if e < maximo:
        maximo = e
print(maximo)        