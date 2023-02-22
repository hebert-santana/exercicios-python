# Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = float(input("Forneça o primeiro número: "))
num2 = float(input("Forneça o segundo número: "))
num3 = float(input("Forneça o terceito número: "))

# Criar uma lista com os números
lista_compara = [num1, num2, num3]

# Ordenar a lista
lista_compara.sort()

# Imprimindo
if lista_compara[0] != lista_compara[1] and lista_compara[0] != lista_compara[2] and lista_compara[1] != lista_compara[2]:
    print(lista_compara[2], " > ", lista_compara[1], " > ", lista_compara[0])
else:
    print("Erro!")
