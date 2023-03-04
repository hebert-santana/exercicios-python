# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

lista = []

n = 0
while n < 10:
    n = n + 1
    numero = int(input("Digite um número: "))
    lista.append(numero)
   
    
par = 0
impar = 0

for num in lista:
    if num % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1
        
print(f'Na lista {lista} há {par} números pares e {impar} números ímpares.')
        
