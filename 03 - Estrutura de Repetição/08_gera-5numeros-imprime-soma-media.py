# Faça um programa que leia 5 números e informe a soma e a média dos números.

from random import randint

numeros_gerados = []
soma = 0
media = 0

# adiciona 5 números aleatórios inteiros entre 0 e 100
for i in range(5):
    num = randint(0, 100)
    numeros_gerados.append(num)
    soma += num

media = soma / len(numeros_gerados)

# imprime resultado      
print(f'Na lista {numeros_gerados}.\nO soma dos números é: {soma}.\nA média dos números é: {media}')