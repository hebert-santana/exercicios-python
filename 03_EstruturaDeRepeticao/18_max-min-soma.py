# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

import random

n = int(input("Conjunto de quantos números? "))

# Gera uma lista de N números inteiros aleatórios
# random.randint(1, 100) gera um número inteiro aleatório entre 1 e 100
# o loop cria uma lista dos N números inteiros aleatórios usando a função randint()
lista_aleatoria = [random.randint(1, 100) for i in range(n)]

# determinando menor e maior valor
menor_valor = min(lista_aleatoria)
maior_valor = max(lista_aleatoria)

# somatório dos valores
def soma(lista):
    soma = 0
    for num in lista:
        soma = soma + num
    return soma

somatorio = soma(lista_aleatoria)
print(f'Conjunto de {n} números: {lista_aleatoria}\n')
print(f'Menor valor: {menor_valor}\nMaior valor: {maior_valor}\nSoma dos valores: {somatorio}\n\n')
        

