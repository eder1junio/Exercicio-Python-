#escreva um progrma que pergumte o valor inicioal de uma divida e o juros mensal. Pergunte tambem o valor mensal que sera pago.sorted
#Imprima o numero de meses para que a dívida seja paga., o total pago e o total de juros pago.
import math
div = int(input("qual o valor inicial da divida ?"))
juros = float(input("qual a taxa de juros mensal "))
pag = float(input("qual o valor pago mensal"))
temp=math.log(pag/(pag-div*(juros/100)))
temp1=math.log(1+juros/100)
temp2 = temp/temp1
print(f'vai demora {temp2:.0f} meses para finaliza a divida')