#rescreva a função para calcularda sequencia fibonacci,sem utiliza recursão.
def fibonacci(n):
    if n <= 0:
        return "N/A - Número inválido"

    fib_sequence = [0, 1]

    for i in range(2, n):
        next_term = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_term)

    return fib_sequence

# Exemplo de uso para obter os primeiros 10 termos da sequência Fibonacci
n = int(input("digite um numero"))
resultado = fibonacci(n)
print(resultado)
