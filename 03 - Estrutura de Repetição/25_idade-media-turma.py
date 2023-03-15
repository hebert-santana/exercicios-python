# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar 
# se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, 
# dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

from random import randint

numero_pessoas = int(input("Número de Pessoas: "))

# Gera uma lista de idades 'inteiras' aleatórias entre 0 e 75
lista_idades = [randint(0, 76) for i in range(numero_pessoas)]
soma_idades = 0

for idade in lista_idades:
    soma_idades += idade

media_idades = round(soma_idades/len(lista_idades))

if media_idades > 60:
    print(f'Turma Idosa. Idade média: {media_idades} anos.')
elif media_idades >= 26:
    print(f'Turma Adulta. Idade média: {media_idades} anos.')
else:
    print(f'Turma Jovem. Idade média: {media_idades} anos.')