# Faça um programa que calcule o mostre a média aritmética de N notas.
from random import randrange

numero_de_notas = int(input("Número de notas: "))

# gera lista de numero_de_notas notas aleatórias entre 0 e 10
lista_notas = [randrange(0, 11) for i in range(numero_de_notas)]
soma = 0

for nota in lista_notas:
    soma += nota

media_das_notas = soma/len(lista_notas)

print(f'Notas: {lista_notas}.\nMédia = {media_das_notas}')