# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

from random import randint

n = int(input("Conjunto de quantos números? "))

lista_numeros = []
soma = 0

for i in range(n):
    numero_aleatorio = randint(0, 1000)
    lista_numeros.append(numero_aleatorio)
    soma += numero_aleatorio


menor = lista_numeros[0]
maior = lista_numeros[0]

for i in range(n):
    if lista_numeros[i] > maior:
        maior = lista_numeros[i]
    if lista_numeros[i] < menor:
        menor = lista_numeros[i]


print(f'Conjunto de {n} números: {lista_numeros}')
print(f'Menor valor: {menor}\nMaior valor: {maior}\nSoma dos valores: {soma}')