# Faça um Programa que leia três números e mostre o maior deles.

n1 = float(input("Forneça o primeiro número: "))
n2 = float(input("Forneça o segundo número: "))
n3 = float(input("Forneça o terceiro número: "))

# cria uma lista com os números
lista_compara = [n1, n2, n3]
print(f'Números fornecido: {lista_compara}')

# ordenar a lista
lista_compara.sort()

# maior número (último da lista ordenada)
print(f'Maior número: {lista_compara[2]}')