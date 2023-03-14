# Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = float(input("Forneça o primeiro número: "))
num2 = float(input("Forneça o segundo número: "))
num3 = float(input("Forneça o terceiro número: "))

# criar uma lista com os números
lista_compara = [num1, num2, num3]

# ordenar a lista
lista_compara.sort()

# pegar o maior e o menor
print(f"Maior: {lista_compara[2]}")
print(f"Menor: {lista_compara[0]}")