# crie um programa que imprima as linha de um arquivo. esse programa deve receber tres parâmetros pela linha de comando 
#:o nome do aquivo, a linha inicial e a ultima a imprimir.
import sys

def imprimatexto(arquivo,liini,lifinal):
    cont = 0 
    
    with open (arquivo, "r") as texto:
        for linha in texto:
            cont +=1
            if cont >= int(liini):
                print(linha,cont)
            if cont == int(lifinal):
                print("ultima linha")
                break    

arquiEntr = sys.argv[1]
inicial = sys.argv[2]
final = sys.argv[3]

imprimatexto(arquiEntr,inicial, final )