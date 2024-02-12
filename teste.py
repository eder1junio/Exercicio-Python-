def obter_opcao_valida(opcoes_validas):
    opcoes_validas = opcoes_validas.lower()
    
    while True:
        escolha = input(f"Escolha uma opção ({opcoes_validas}): ").upper()
        
        if escolha in opcoes_validas:
            return escolha
        else:
            print("Opção inválida. Tente novamente.")

# Exemplo de uso:
opcoes_validas = "ABC"
opcao_escolhida = obter_opcao_valida(opcoes_validas)
print(f"Opção escolhida: {opcao_escolhida}")