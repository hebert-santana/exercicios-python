# Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = float(input("Forneça o primeiro número: "))
n2 = float(input("Forneça o segundo número: "))
n3 = float(input("Forneça o terceito número: "))

lista_compara = [n1, n2, n3]
lista_compara.sort()

if n1 != n2 and n1 != n3 and n2 != n3:
    print(lista_compara[2], " > ", lista_compara[1], " > ", lista_compara[0])
else:
    print("Erro!")
