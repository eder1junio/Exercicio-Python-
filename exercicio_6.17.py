#altere o Programa 6.22 de forma a solicitar ao usuario o produto e a quantidade vendida.VERIFIQUE SE O NOME DO PRODUTO EXISTE NO 
#dicionario e so entao efetue a baixa do estoque.
estoque = {"tomate": [1000,2.30],
           "alface":[500,0.45],
           "batata":[2001,1.20],
           "feijão":[100,1.50]}
print(estoque)
venda = []
while True:
    venda.append(str(input('qual a verdura foi vendida')))
    venda.append(int(input('quantidade vendida')))
    if venda[0] in estoque:
        total = 0
        print("venda:\n")
        print(f"Produto:{venda[0]}qunatidade {venda[1]}")
        estoque[venda[0]][0]=estoque[venda[0]][0] -venda[1]

        #for operacao in venda:
        #    produto, quantidade = operacao
        #    preco = estoque[produto][1]
        #    custo = preco * quantidade
        #    print(f"{produto:12s}:{quantidade:3d}x{preco:6.2f}= {custo:6.2f}")
        #    estoque[produto][0]-= quantidade
        #   total += custo
        #print(f"custo total:{total:21.2f}\n")
        #print("Estoque:\n")
        for chave, dados in estoque.items():
            print("Descrição:",chave)
            print("quantidade:",dados[0])
            print(f"Preço:{dados[1]:6.2f}\n")
        break    
    else:
        print('digite um verdura valida ')            