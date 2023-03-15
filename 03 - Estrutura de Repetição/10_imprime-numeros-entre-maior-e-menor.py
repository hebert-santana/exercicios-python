# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

n1 = int(input("Primeiro Número: "))
n2 = int(input("Segundo Número: "))

menor = n1
maior = n2

if n2 < n1:
    menor = n2
    maior = n1

diferenca = maior - menor
print(f'Números inteiros entre {menor} e {maior}:')

numero_intervalo = menor + 1

while diferenca != 1:
    print(numero_intervalo)
    numero_intervalo += 1
    diferenca -= 1