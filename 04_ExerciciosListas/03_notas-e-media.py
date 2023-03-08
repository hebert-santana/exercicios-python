# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []

for i in range(1, 5):
    notas.append(float(input(f'Informe a nota {i}: ')))
    
media = sum(notas)/len(notas)

print(f'Notas: {notas}\nMédia = {media}')