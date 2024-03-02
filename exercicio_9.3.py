#crie um progrma que leia os aquivo pare.txt e impares.txt e crie um  só 
#arquivo paresimpares.txt com todos as linha dosOUTRO DOIS AQUIVOS de forma a 
#presevara ordem numerica.
with open("impares.txt","r") as impares :
    impares = impares.readlines()
    with open("pares.txt","r") as pares: 
        pares = pares.readlines()
        with open("imp_par.txt","w") as imp_par:
            for t in range(max(len(impares),len(pares))):
                    imp_par.write(f"{pares[t]}\n")  
                    imp_par.write(f"{impares[t]}\n")      

                


        