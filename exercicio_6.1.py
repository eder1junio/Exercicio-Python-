#Modifique o Programa 6.2 para ler 7 notas em vez de 5.
notas = [0,0,0,0,0,0,0]
soma = 0
x =0
while x < 7:
    notas[x] = float(input(f'Digite a {x+1}º nota '))
    soma +=notas[x] 
    x+=1
x = 0   
while x < 7:
    print(f' {x+1}ª nota e {notas[x]:6.2f}')
    x+=1
print(f'media:{soma/x:5.2f}')      