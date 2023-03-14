# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. 
# Imprima as consoantes.

import random
import string

# random.choice() escolher um elemento aleatório de uma sequência
# string.ascii_lowercase retorna as letras do alfabeto (minúsculas)
# for i in range(10) - executar 10x o loop
vetor_letras_aleatorias = list(random.choice(string.ascii_lowercase) for i in range(10))

print(f'Lista Original: {vetor_letras_aleatorias}')

vogais = ['a', 'e', 'i', 'o', 'u']

# contador de consoantes
numero_consoantes = 0
# lista de consoantes
lista_consoantes = []

for i in vetor_letras_aleatorias:
    if i not in vogais:
        numero_consoantes = numero_consoantes + 1
        lista_consoantes.append(i)
        
print(f'Número de consoantes: {numero_consoantes}\nLista das consoantes: {lista_consoantes}.')


# Consonates sem repetição:
lista_consoantes_sr = set(lista_consoantes)
num_consoantes_sr = len(lista_consoantes_sr)
print(f'Número de consoantes sem repetição: {num_consoantes_sr}\nLista das consoantes sem repetição: {lista_consoantes_sr}.')
        
        
    
    