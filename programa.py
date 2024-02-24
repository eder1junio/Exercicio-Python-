import sys

# Verifica se o nome do arquivo foi fornecido como argumento na linha de comando
if len(sys.argv) < 2:
    print("Uso: python programa.py nome_do_arquivo")
    sys.exit(1)

# Obtém o nome do arquivo a partir dos argumentos da linha de comando
nome_arquivo = sys.argv[1]

try:
    # Abre o arquivo especificado
    with open(nome_arquivo, "r") as arquivo:
        # Lê e imprime todas as linhas do arquivo
        for linha in arquivo:
            print(linha, end="")
except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")