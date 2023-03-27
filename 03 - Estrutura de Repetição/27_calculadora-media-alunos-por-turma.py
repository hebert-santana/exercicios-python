# Faça um programa que calcule o número médio de alunos por turma. 
# Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. 
# As turmas não podem ter mais de 40 alunos.

qnt_turmas = int(input('Digite a quantidade de turmas: '))
total_alunos = 0

for i in range(1, qnt_turmas+1):
    while True:
        qnt_alunos = int(input(f'Digite a quantidade de alunos na turma {i}: '))
        if qnt_alunos <= 40:
            break
        else:
            print('A turma não pode ter mais de 40 alunos.')
    total_alunos += qnt_alunos

media_alunos = total_alunos / qnt_turmas
print(f'A média de alunos por turma é de: {media_alunos:.2f}')
