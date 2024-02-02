#escreva uma função que receba o lado de um quadrado e retorne sua area a= lado². valor esperado area_quadrada (4) == 16, 
#area_quadrada(9)==81

def area_quadrada(t):
    return t*t

t = int(input("qua o comprimento do lado do quadrado"))
print(area_quadrada(t))