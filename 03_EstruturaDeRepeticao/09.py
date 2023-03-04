# Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

lista_numeros = list(range(1, 51))

# se o número não é par, imprime
for num in lista_numeros:
    if num % 2 != 0:
        print(num)