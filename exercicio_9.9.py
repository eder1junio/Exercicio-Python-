#crie um programa que receba uma lista  de nome de aruivo e os imprima, um por um. 
import time
with open('nomes.txt', 'r') as nomes:
    nomes1 = nomes.readlines()
    for nomes2 in nomes1:
        print(nomes2)
        time.sleep(1)