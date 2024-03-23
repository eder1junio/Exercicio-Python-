#crie um programa  que leia um arquivo e crie um dicionario em quE cada chave e uma palavra e cada valor
#e o numero de ocorrencia no aquivo

def contaPala(arquivo):
    dicio = {}
    with open (arquivo , "r") as arquivo1:
        for linha in arquivo1:
            for palavras in linha.split():
                palavras = palavras.strip(".!?").lower()
                if palavras in dicio:
                    dicio[palavras] +=1
                else :
                    dicio[palavras] = 1
    return dicio                                  


print(contaPala("textoalea.txt"))