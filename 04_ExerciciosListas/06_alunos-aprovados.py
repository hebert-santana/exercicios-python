# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

import random

alunos = []

# cria lista com 10 alunos
for i in range(1,11):
    alunos.append(f"Aluno {i}")
    
aprovados = 0
 
# cria 4 notas para os alunos
for aluno in alunos:
    # criando lista com 4 notas
    notas = list(random.randint(0, 10) for i in range(4))
    # média das 4 notas
    media = sum(notas) / len(notas)
    print(f'{aluno} teve a média: {media}')
    if media >= 7:
        aprovados = aprovados + 1
        
print(f'Número de aprovados: {aprovados}')