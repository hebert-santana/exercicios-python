# Faça um programa que leia 5 números e informe o maior número.

import random

lista_numeros = []


for num in range(5):
    numero = random.randint(0, 100) # números aleatórios entre 0 e 100
    lista_numeros.append(numero)
    

lista_numeros.sort

print(lista_numeros[-1])
    
    