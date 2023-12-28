#a lista de temperatura de mons, na belgica foi armagenada na lista t = [-10,-8,0,1,2,5,-2,-4]. Faça um progrma que imprima a menor 
# e a maior temperatura , assim como a temperatura media.
t = [-10,-8,0,1,2,5,-2,-4]
maior = menor = t[0]
soma = media = 0

for n in t:
    if n > maior:
        maior = ns
    if n < menor:
        menor = n
    soma += n  
media = soma /len(t)       

print(f"a maior temperatura e {maior} a menor temperatura e {menor} a media da temperatura e {media}")
