# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

from random import randint

n = int(input("Conjunto de quantos números? "))

lista_numeros = []
soma = 0

for i in range(n):
    numero_aleatorio = randint(1, 100)
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
        

