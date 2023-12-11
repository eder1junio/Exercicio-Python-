#escreva um programa de leia numeros inteiro do teclado. o Progrma de ler os numero ate que o usuario digite 0.
# No final da execução exiba a quatidade de numeros digitados, assim comoa soma e a media aritimetica.
cont = 0
soma = 0
media =0
while True:
    num = int(input('DIGITE UM NUMERO QUAQUER'))
    if num == 0:
        break
    cont+=1
    soma += num
    media = soma/cont

print(f"a soma dos numeros digitadoe e {soma} a média e {media:.2f}")


