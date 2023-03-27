# Faça um Programa que leia dois vetores com 10 elementos cada. 
# Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

a = []
b = []
c = []

# lendo os valores do vetor a
for i in range(10):
    valor = int(input(f'Digite o {i+1}º valor do vetor A: '))
    a.append(valor)

# lendo os valores do vetor b
for i in range(10):
    valor = int(input(f'Digite o {i+1}º valor do vetor B: '))
    b.append(valor)

# gerando o vetor c
for i in range(10):
    c.append(a[i])
    c.append(b[i])

# imprime o resultado de c
print('Vetor C: ', end='')
print(c)
