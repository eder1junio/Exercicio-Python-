#Escreva uma função que receba dos numeros e retorne True se o primeiro for multiplo do primeiro. valores esperadoes multiplo(8,4) == True
#multiplo(7,3) == False, Multiplo(5,5) == TR

def multiplo(n1,n2):
  if n2!=0:
    if n1%n2 == 0:  
        return True
    else:
       return False
n1 = int(input("digite um numero "))
n2 = int(input("digite outro numero"))    

n3 = multiplo(n1,n2)
print(n3)
