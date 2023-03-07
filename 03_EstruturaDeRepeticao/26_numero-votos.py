# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
import random

num_eleitores = int(input("Número de eleitores: "))

# número de votos
candidato_A = 0
candidato_B = 0
candidato_C = 0

# lista com num_eleitores votos entre opção 1 e opção 3
lista_dos_votos = [random.randint(1, 3) for i in range(num_eleitores)]

# contando votos
for voto in lista_dos_votos:
    if voto == 1:
        candidato_A = candidato_A + 1
    elif voto == 2:
        candidato_B = candidato_B + 1
    else:
        candidato_C = candidato_C + 1
        
print(f'RESULTADO:\nVotos em A: {candidato_A} votos.\nVotos em B: {candidato_B} votos.\nVotos em C: {candidato_C} votos.')