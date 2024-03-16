#crie  um programa que leia  um arquivo-texto  e gere um aquivo de saida paginado,  cada linha nao deve conter 
#mais de 76 caracteres. Cada pagina  tera no maximo 60 linha. adcione na ultima linha de cada pagina o numero
# da pagina atual e o nome do arquivo original.

linha = 0
paj = 0
def formata(texto):
    cont =0
    with open( texto,'r') as texto:
        with open('textofor.txt', 'w') as textofor:
            texto = texto.readlines()
            for linha in range(len(texto)):
                texto1 = texto[linha].strip()
                print(texto1)
                for letra in texto1:
                    if cont < 76:
                        textofor.write(letra)
                        cont +=1
                    if cont == 76:  
                        textofor.write('\n')
                        cont = 0 

def formatapaj(texto2):
     linha1 = 0
     paj = 0
     with open( texto2,'r') as texto:
        with open('textofor1.txt', 'w') as textofor1:
            texto = texto.readlines()
            for linha in texto:
                textofor1.write(linha)
                linha1 +=1
                if linha1 == 60:
                    paj+=1
                    textofor1.write('\n')
                    textofor1.write(f'Pagina {paj} Texto de Eder \f')
                    textofor1.write('\n')
                    linha1 = 0
                    
def formatar_e_numerar_paginas(texto):
    linha1 = 0
    contador_caracteres = 0
    paj = 0
    with open(texto, 'r') as arquivo_entrada:
        with open('textofor2.txt', 'w') as textofor2:
            for linha in arquivo_entrada:
                for letra in linha.strip():
                    textofor2.write(letra)
                    contador_caracteres += 1
                    if contador_caracteres == 76:
                        textofor2.write('\n')
                        contador_caracteres = 0
                linha1 += 1
                if linha1 == 60:
                    paj += 1
                    textofor2.write(f'\nPagina {paj} Texto de Eder \f\n')
                    linha1 = 0
            if contador_caracteres > 0:
                textofor2.write('\n')                    
               
                    

formata("textoalea.txt") 
formatapaj("textofor.txt")                