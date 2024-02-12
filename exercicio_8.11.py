#escreva uma função para validar uma variavel string.essa função recebe como parametro a string.
#o numero minimo e o maximo caracteres. retorne verdadeiro se o tamanho da string estive entre o tamanho e o minimo,
#falso caso contrario.

def stringMaxMin(stri1,max,min):
    if len(stri1)>min and len(stri1)<max:
        return True
    else:
        return False
    
print(stringMaxMin("eder",10,6))    