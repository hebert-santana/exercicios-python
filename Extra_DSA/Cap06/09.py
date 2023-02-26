# Exercício 9 - Considere a lista abaixo e retorne apenas os elementos cujo índice for maior que 5.
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# usando a função enumerate
lista_tuplas = list(enumerate(lista))
print("Lista de Tuplas:", lista_tuplas)

# imprimindo valores conforme condição
for chave, valor in lista_tuplas:
    if chave > 5:
        print(valor)