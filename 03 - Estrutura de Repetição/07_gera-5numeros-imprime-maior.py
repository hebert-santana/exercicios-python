# Faça um programa que leia 5 números e informe o maior número.

from random import randint

# adiciona 5 números aleatórios inteiros entre 0 e 100
maior = 0
numeros_gerados = []
for i in range(5):
    n = randint(0, 100)
    numeros_gerados.append(n)
    if n > maior:
        maior = n

print(f'Números gerados: {numeros_gerados}')
print(f'O maior valor gerado foi: {maior}.')


    
    