#escreva uma função que receba uma string e uma lista. a função deve compara a string passada com os elementos da lista.
#tambem passado como parametro. Retorne verdadeiro se a string fo encontrado dentro da lista. e falso caso contrario.

def nome (n, lista):
    if n in lista:
        return True
    else:

        return False
    
n = "joao"
lista = ["eder", "sanba", "livro", "junio", "marua"] 
print(nome(n,lista))   