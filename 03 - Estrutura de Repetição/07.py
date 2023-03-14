# Faça um programa que leia 5 números e informe o maior número.

# importando pacote para usar função randint
import random

# cria lista vazia
lista_numeros = []

# adiciona 5 números aleatórios inteiros entre 0 e 100
for num in range(5):
    numero = random.randint(0, 100)
    lista_numeros.append(numero)

# maior valor inicial é elemento de índice 0   
maior_numero = lista_numeros[0]

# percorre a lista em busca do maior valor
for num in lista_numeros:
    if num > maior_numero:
        maior_numero = num

# imprime resultado      
print(f'Na lista {lista_numeros}.\nO maior valor é: {maior_numero}.')


    
    