# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

num1 = float(input("Preço produto 1: "))
num2 = float(input("Preço produto 2: "))
num3 = float(input("Preço produto 3: "))

# Criar uma lista com os números
lista_compara = [num1, num2, num3]

# Ordenar a lista
lista_compara.sort()

if lista_compara[0] == num1:
    print("Comprar o Produto 1.")
elif lista_compara[0] == num2:
    print("Comprar o Produto 2.")
elif lista_compara[0] == num3:
    print("Comprar o Produto 3.")
else:
    print("Erro!")
