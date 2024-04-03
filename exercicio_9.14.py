#crie um prpgrama  que leia um aquivo-texto e elimine os espaços repetidos entre as palavras e no fim 
#da linha. o aquivo de saida tambem nao deve ter mais de uma linha em branço repetida.

cont = 1
with open(aquivo , "r") as aquivoAber:
    with open("textoform.txt", "w") as texto:
        for linha in aquivoAber:
            linha = linha.strip()
            for letra in linha:
                if letra == " ":
                    cont+=1
                    if cont==2:
                        cont =0
                        continue
                texto.write(letra)    
                        