#escrega um programa que gere um dicionário, em que cada chave seja um caractere, e seu valor seja um numero desse
#caractere encontrado em uma frase lida.

frase = str(input('Escreva uma frase'))
LetraPletra = {}
#for n in frase:
#    LetraPletra [n] = ord(n)

#print(LetraPletra)
for n in frase:
    if n not in LetraPletra:
        LetraPletra[n] = 0

    if n in LetraPletra:
        LetraPletra[n] = LetraPletra[n] + 1
print(LetraPletra)        