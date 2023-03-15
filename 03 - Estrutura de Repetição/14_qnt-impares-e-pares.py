# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

 

qnt_p = 0
qnt_i = 0
numeros_digitados = []

for x in range(10):
    n = int(input('Digite um número: '))
    numeros_digitados.append(n)
    if n % 2 == 0:
        qnt_p += 1
    else:
        qnt_i += 1
        
print(f'Números digitados: {numeros_digitados}')
print(f'Quantidade pares: {qnt_p}')
print(f'Quantidade impares: {qnt_i}')
    
        
