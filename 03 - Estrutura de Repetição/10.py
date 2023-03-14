# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

num1 = int(input("Primeiro Número: "))
num2 = int(input("Segundo Número: "))

menor = num1
maior = num2

if num2 < num1:
    menor = num2
    maior = num1

lista = list(range((menor+1), maior))

print(f'\n-------------------------------------\n\nNúmeros inteiros entre {menor} e {maior}:')

for num in lista:
    print(num, end=' ')