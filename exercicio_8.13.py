#escreva uma função que receba uma string com as opcoes validas a aceita(cada opcão e uma letra).Converte as opçoes
#validas para letrasminusculas.Utilize input para lea uma opçaõ, converte o valor para letras maisculas 
#e verificar se a opção valida. em caso de opção invalida, afunçã deve pedir ao usuario que digitr novamente outra opção.

def opcoes(op):
    op_validas = op.lower()
    while True:
        opt = str(input(f"digite uma opção{op_validas}")).lower()       
        if opt.isalpha() and opt in op_validas:
            print("opção valida")
            break
        else:
            print("opção invalida")
            continue

opcoes("abcd")

