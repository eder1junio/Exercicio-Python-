#crie um programa que invere a ordem das linha do aquivo pares.txt. a primeira linha deve conter o maior valora
#e o ultimo o menor.
def invert(aquivo):
    with open(aquivo,"r") as aquivo1:
        with open("invertido.txt","w") as invertido:
            le = aquivo1.readlines()
            for t in range(len(le)-1,-1,-1):
                invertido.write(f"{le[t]}")

def invert1(aquivo):
    with open(aquivo,"r") as aquivo1, open("invertido1.txt","w") as invertido:
        le = aquivo1.readlines()
        le.reverse()
        for linha in le:
            invertido.write(linha)


invert1("pares.txt")