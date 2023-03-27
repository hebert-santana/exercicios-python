# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

vetor = []
soma_quadrados = 0

# lendo 10 valores para o vetor
for i in range(10):
    valor = int(input(f'Digite o {i+1}º valor: '))
    vetor.append(valor)

# calculando a soma dos quadrados dos valores
for i in vetor:
    soma_quadrados += i ** 2

# imprimindo o resultado
print(f'A soma dos quadrados dos elementos do vetor é: {soma_quadrados}')
