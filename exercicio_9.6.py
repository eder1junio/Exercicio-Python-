#Modifique o progrma 9.5 para imprimir 40 vezes o simbolo de = se este for o primeiro caractere da linha
#adcione tambem a opção  para parar de imprimir ate que se pressione a tecla enter cada vez que uma linha inicia com
#ponto(.)como primeiro caractere.
import keyboard
LARGURA = 79
cont = 0
with open("entrada.txt") as entrada:
    for linha in entrada.readlines():
        if linha[0]==";":
            continue
        elif linha[0] ==">":
         print(linha[1:].rjust(LARGURA))
        elif linha[0]== "*":
           print(linha[1:].center(LARGURA))
        elif linha[0]=="=":
           while cont <= 40:  
              print(linha[1:])
              cont+=1 
        elif linha[0] == "!":
            print("precione enter para para")
            while True:
                print(linha[1:])
                if  keyboard.is_pressed("enter"):
                    print("loop parado") 
                    break
                  
        else:
           print(linha)   