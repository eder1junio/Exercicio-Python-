#escreva umj programa que leia duas string e gere uma terceira, a qual os caracteres da segunda foram tirada da primeira.
#1ª string: aattggaa 2ª string tg 3º atring: aaaa

n = list(input("digite alguma palavra"))
n1 = input("digite outra palavra")
for a in n1:
    cont = 0
    while True: 
        if cont == len(n):
            break   
        if a == n[cont]:
           del n[cont]
        cont +=1
n2 = "".join(n)       
print(n2)           
