# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
# Imprima os três vetores.

import random

vetor = []

for i in range(20):
    num = random.randint(1, 100) # números inteiros de 1 a 100
    vetor.append(num)

# ordenar o vetor
vetor.sort()
    
print(f'Vetor original: {vetor}')

vetor_par = []
vetor_impar = []

for n in vetor:
    if n % 2 == 0:
        vetor_par.append(n)
    else:
        vetor_impar.append(n)
        
# ordenar os vetores
vetor_par.sort()
vetor_impar.sort()
   
print(f'Vetor par: {vetor_par}')
print(f'Vetor impar: {vetor_impar}')
