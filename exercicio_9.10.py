#Crie um programa que receba uma lista de nome de aquivo e que gere apena um grande aquivo de saida.

def juntaaquivo(*varios):
    for aqui in varios:
        with open(aqui,"r") as arqui1:
            with open( "arquivp.txt" ,"a") as arqui:
                for linha in arqui1:
                    arqui.write(linha)

juntaaquivo("textofor.txt","textofor2.txt")