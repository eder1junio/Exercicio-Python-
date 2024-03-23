#Modifique o progrma do exercicio 9.7 para tambem recebe o numero de caracteres por linha e o numero 
#de linha por paginas  pela linha de comando 
import sys
def formatar_e_numerar_paginas(texto,cara,linha4):
    linha1 = 0
    contador_caracteres = 0
    paj = 0
    with open(texto, 'r') as arquivo_entrada:
        with open('textofor2.txt', 'w') as textofor2:
            for linha in arquivo_entrada:
                linha1 += 1
                for letra in linha.strip():
                    textofor2.write(letra)
                    contador_caracteres += 1
                    if contador_caracteres == cara:
                        textofor2.write('\n')
                        contador_caracteres = 0
                linha1 += 1        
                if linha1 == linha4:
                    paj += 1
                    textofor2.write(f'\n')
                    textofor2.write(f'\nPagina {paj} Texto de Eder \f\n')
                    textofor2.write(f'\n')
                    linha1 = 0
            if contador_caracteres > 0:
                textofor2.write('\n')   

if len(sys.argv)!= 4:
    print("por favor 1ª nome do aquivo 2ª aquivo a ser processado") 
    print("3º quantidade de caracteres por linhas 4º numeros de linha por paginas ")
texto1 = sys.argv[1]
cara = int(sys.argv[2])
linha4 = int(sys.argv[3])     
formatar_e_numerar_paginas(texto1,cara,linha4) 
print("fim")             