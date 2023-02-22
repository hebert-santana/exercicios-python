# Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = float(input("Forneça o primeiro número: "))
num2 = float(input("Forneça o segundo número: "))
num3 = float(input("Forneça o terceiro número: "))

# Criar uma lista com os números
lista_compara = [num1, num2, num3]

# Ordenar a lista
lista_compara.sort()

# Pegar o maior e o menor
print("Maior: ", lista_compara[2])
print("Menor: ", lista_compara[0])