#Escreva um progrma que leia uma string e imprima quantas vezes cada caractere aparece nessa string.
#String : ttaac resultado t:2 a: 2x c:1x
letras = {}
st = input("digite alguma coisa")
for a in st:
    if a not in letras:
        letras[a] = st.count(a)

print(letras)

