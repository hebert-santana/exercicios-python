# Foram anotadas as idades e alturas de 30 alunos. 
# Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

idades = []
alturas = []

# lendo idades e alturas dos 30 alunos
for i in range(30):
    idade = int(input(f'Informe a idade do {i+1}º aluno: '))
    altura = float(input(f'Informe a altura do {i+1}º aluno: '))
    idades.append(idade)
    alturas.append(altura)

# calculando a media das alturas dos alunos com mais de 13 anos
alturas_maiores_13 = [alturas[i] for i in range(30) if idades[i] > 13]
media = sum(alturas_maiores_13) / len(alturas_maiores_13)

# contagem dos alunos com mais de 13 anos e altura inferior à média obtida da altura
contador = 0
for i in range(30):
    if idades[i] > 13 and alturas[i] < media:
        contador += 1

# imprime o resultado
print(f'{contador} alunos com mais de 13 anos possuem altura inferior à média de altura dos alunos com essa faixa etária.')
