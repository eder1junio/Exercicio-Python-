#Modifique o progrma do exercicio 9.11 para tambem registrar a linha e a coluna de cada ocorrencia
#da palavra no aquivo. para isso, utilize lista no s valores de cada palavra, guardando a linha e a 
#coluna de cada ocorrencia  

def contaPala(arquivo):
    dicio = {}
    linha = 0
    with open (arquivo , "r") as arquivo1:
        for linha_n , linha in enumerate(arquivo1,start=1):
            for pala_n ,palavras in enumerate(linha.split(),start=1):
                palavras = palavras.strip(".!?").lower()
                if palavras in dicio:
                    dicio[palavras].append((linha_n,pala_n))
                else:
                    dicio[palavras] = (linha_n,pala_n)
    return dicio                                  


print(contaPala("textoalea.txt"))