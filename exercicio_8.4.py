#escreva uma função que receba a base e a altura de um triângulo e retorne sua Area(a = (base*altura)/2).
#valores esperados: area_triangulo(6,9)== 27, area_triagulo(5,8) ==20

def area_triagulo(b,a):
    return (b*a)/2

b = int(input("qual a base do triâgulo"))
a = int(input("qual a altura do triagulo"))

print(area_triagulo(b,a))