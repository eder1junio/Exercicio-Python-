#escreva um programa que leia duas string gere uma terceira com apenas  com os caracteres que aparecem em uma delas.
#1ºstring: CTE 1º string :ABC 3ºstring: BT A ordem dos caracteres da terceira string nao e importante:]

n = "a maria beijou joao"
n2 = "o carro esta parado"

set_string1= set(n)
set_string2 = set(n2)
cart_com = set_string1- set_string2
cart_com2 = set_string2 - set_string1
n3 = cart_com.union(cart_com2)
n4 = "".join(n3)


print(f"{n} {n2} {n3} {n4}")
