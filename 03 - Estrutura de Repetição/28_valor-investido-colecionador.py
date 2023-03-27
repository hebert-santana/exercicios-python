# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. 
# O usuário deverá informar a quantidade de CDs e o valor para em cada um.

qnt_CDs = int(input('Informe a quantidade de CDs na coleção: '))

valor_total = 0
for cd in range(1, qnt_CDs + 1):
    preco = float(input(f'Informe o preço do CD {cd}: R$ '))
    valor_total += preco
    
media = valor_total / qnt_CDs

print(f'Valor total: {valor_total}')
print(f'Média por CD: {media}')