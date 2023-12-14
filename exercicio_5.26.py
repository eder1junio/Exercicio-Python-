#escreva um programa que calcule o resto da divisão inteira entre dois numeros.Utilizando
#apenas operação de soma e subtração para calcular o resultado.
n = int(input("digite o primeiro numeor"))
n2 = int(input('digite o segundo numeor'))
resto = n
while n2 < resto:
    resto -= n2
print(f"{n}/{n2} tem Resto {resto}")    