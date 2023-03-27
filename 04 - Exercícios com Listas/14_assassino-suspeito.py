# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# 'Telefonou para a vítima?'
# 'Esteve no local do crime?'
# 'Mora perto da vítima?'
# 'Devia para a vítima?'
# 'Já trabalhou com a vítima?' 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como 'Suspeita', entre 3 e 4 como 'Cúmplice' e 5 como 'Assassino'. 
# Caso contrário, ele será classificado como 'Inocente'.

print('Responda\n[S] - sim\n[N] - não')
respostas = []
respostas.append(input('Telefonou para a vítima? ').upper().strip()[0])
respostas.append(input('Esteve no local do crime? ').upper().strip()[0])
respostas.append(input('Mora perto da vítima? ').upper().strip()[0])
respostas.append(input('Devia para a vítima? ').upper().strip()[0])
respostas.append(input('Já trabalhou com a vítima? ').upper().strip()[0])

# contando respostas 'sim'
contador = respostas.count('S')

# classificando 
if contador == 2:
    print('Pessoa suspeita')
elif contador in [3, 4]:
    print('Pessoa cúmplice')
elif contador == 5:
    print('É o assassino')
else:
    print('É inocente')
