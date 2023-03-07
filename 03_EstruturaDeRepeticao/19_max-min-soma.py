# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

import random

n = int(input("Conjunto de quantos números? "))

lista_aleatoria = [random.randint(0, 10001) for i in range(n)]

menor_valor = min(lista_aleatoria)
maior_valor = max(lista_aleatoria)


def soma(lista):
    soma = 0
    for num in lista:
        soma = soma + num
    return soma

somatorio = soma(lista_aleatoria)


print(f'Conjunto de {n} números: {lista_aleatoria}\n')
print(f'Menor valor: {menor_valor}\nMaior valor: {maior_valor}\nSoma dos valores: {somatorio}\n\n')