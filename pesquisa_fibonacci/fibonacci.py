import math


# Função que verifica se n é um quadrado perfeito.
def quadradoPerfeito(x):
    raiz = int(math.sqrt(x))
    return raiz * raiz == x


# Verifica se número n pertence à série de Fibonacci
# n é Fibonacci se o resultado de 5*n*n + 4 ou 5*n*n - 4 ou ambos
# forem quadrados perfeitos.
def eFibonacci(n):
    return quadradoPerfeito(5 * n * n + 4) or quadradoPerfeito(5 * n * n - 4)


if __name__ == '__main__':
    n = int(input('Digite um número qualquer, positivo: '))

    if (eFibonacci(n)):
        print(f"{n} pertence à série de Fibonacci.")
    else:
        print(f"{n} não pertence à série de Fibonacci.")