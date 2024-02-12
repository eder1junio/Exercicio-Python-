#altere  programa 7.2 o jogo da forca. escolha a palavra e adivinhe  ultilizando o numero aleatorio.

#palavra = input("digite a palavra secreta").lower().strip()
import random
listaPal = ["terra", "amor", "parede", "arvore", "brinquedo"]
palavra = " ".join(random.sample(listaPal,1))
print(palavra)
for x in range(2):
    print()
digitadas = []
acerto = []
erros = 0 
while True:
    senha = " "
    for letra in palavra:
        senha += letra if letra in acerto else "."
    print(senha)
    if senha == palavra:
        print("voce acertou")
        break
    tentativa = input("\nDigite uma Letra:").lower().strip()
    if tentativa in digitadas:
        print("voce ja tentou esta letra")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acerto += tentativa
        else:
            erros+=1
            print("voce errou ")
        print("X==:==\nX    :   ")
        print("x  0"if erros >=1 else "x")
        linha2 = ""
        if erros == 2:
            linha2 ="  |   "
        elif erros == 3:
            linha2 = "  \|  "
        elif erros >= 4:
            linha2 = " \|/"
        print(f"x{linha2}")
        linha3 =""
        if erros == 5:
            linha3 +=" /"
        elif erros == 6:
            linha3 += " / \ "
        print(f"x{linha3}")
        print("x\n============") 
        if erros == 6:
            print("Enforcado")
            break 


