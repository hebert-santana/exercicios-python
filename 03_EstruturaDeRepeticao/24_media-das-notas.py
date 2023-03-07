# Faça um programa que calcule o mostre a média aritmética de N notas.
import random

numero_de_notas = int(input("Número de notas: "))

# Gera uma lista de numero_de_notas notas aleatórias entre 0 e 10
lista_notas = [random.randrange(1, 11) for i in range(numero_de_notas)]

soma_das_notas = 0
for nota in lista_notas:
    soma_das_notas = soma_das_notas + nota

media_das_notas = soma_das_notas/len(lista_notas)

print(f'Notas: {lista_notas}.\nMédia = {media_das_notas}')