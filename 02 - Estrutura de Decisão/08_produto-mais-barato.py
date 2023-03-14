# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

n1 = float(input("Preço produto 1: "))
n2 = float(input("Preço produto 2: "))
n3 = float(input("Preço produto 3: "))

# lista com os números
lista_compara = [n1, n2, n3]

# ordenar a lista
lista_compara.sort()

if lista_compara[0] == n1:
    print(f"Comprar o Produto 1.\nPreço: {n1}.")
elif lista_compara[0] == n2:
    print(f"Comprar o Produto 2.\nPreço: {n2}.")
elif lista_compara[0] == n3:
    print(f"Comprar o Produto 3.\nPreço: {n3}.")
else:
    print("Erro!")
