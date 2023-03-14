# Faça um programa que leia 5 números e informe a soma e a média dos números.

# importando pacote para usar função randint
import random

# cria lista vazia
lista_numeros = []

# adiciona 5 números aleatórios inteiros entre 0 e 100
for num in range(5):
    numero = random.randint(0, 100)
    lista_numeros.append(numero)

# soma inicial = 0   
soma = 0

# percorre a lista e soma valores
for num in lista_numeros:
    soma = soma + num
    
# encontrar a média
media = soma / len(lista_numeros)

# imprime resultado      
print(f'Na lista {lista_numeros}.\nO somatório é: {soma}.\nA média é: {media}')