# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
# Imprima a idade e a altura na ordem inversa a ordem lida.

# idade e a altura de 5 pessoas
idades = []
alturas = []

for i in range(5):
    idade = int(input(f'Digite a idade da {i+1}ª pessoa: '))
    altura = float(input(f'Digite a altura da {i+1}ª pessoa: '))
    idades.append(idade)
    alturas.append(altura)

idades_reversas = list(reversed(idades[:]))
alturas_reversas = list(reversed(alturas[:]))


# imprime as idades na ordem inversa
print('Idades na ordem inversa: ', end='')
for i in idades_reversas:
    print(i, end=' ')
    

# imprime as alturas na ordem inversa
print('\nAlturas na ordem inversa: ', end='')
for i in alturas_reversas:
    print(i, end=' ')
