# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

a = []
b = []
c = []
d = []

for i in range(10):
    valor = int(input(f'Digite o {i+1}º valor do vetor A: '))
    a.append(valor)

for i in range(10):
    valor = int(input(f'Digite o {i+1}º valor do vetor B: '))
    b.append(valor)

for i in range(10):
    valor = int(input(f'Digite o {i+1}º valor do vetor C: '))
    c.append(valor)

for i in range(10):
    d.append(a[i])
    d.append(b[i])
    d.append(c[i])

print('Vetor D: ', end='')
print(d)
