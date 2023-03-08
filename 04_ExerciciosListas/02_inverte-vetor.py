# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

vetor = []

for i in range(0, 10):
    vetor.append(float(input('Informe um numero: ')))

# invertendo a ordem
vetor.reverse()

print(vetor)