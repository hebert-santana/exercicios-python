# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

# lendo vetor de 5 numeros inteiros
vetor = []
for i in range(5):
    n = int(input(f'Digite o {i+1}º número: '))
    vetor.append(n)

# mostrando os numeros digitados
print('Números digitados: ', end='')
for n in vetor:
    print(n, end=' ')

# soma
soma = sum(vetor)
print(f'\nA soma dos números é: {soma}')

# multiplicação
mult = 1
for n in vetor:
    mult *= n
print(f'A multiplicação dos números é: {mult}')
