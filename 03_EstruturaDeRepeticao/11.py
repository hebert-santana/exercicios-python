# Altere o programa anterior para mostrar no final a soma dos números.

num1 = int(input("Primeiro Número: "))
num2 = int(input("Segundo Número: "))

menor = num1
maior = num2

if num2 < num1:
    menor = num2
    maior = num1

lista = list(range((menor+1), maior))

somatorio = 0
for num in lista:
    somatorio = somatorio + num

print(f'-------------------------------------\nSomatório dos inteiros entre {menor} e {maior}: {somatorio}')

