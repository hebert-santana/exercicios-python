# Exercício 6 - Considerando o range de valores abaixo, use a função filter() para retornar apenas os valores negativos.
range(-5, 5)

# criando lista conforme o range
lista_original = list(range(-5, 5))
print("Lista Inicial: ")
print(lista_original)

# obtendo a lista filtrada conforme critério
lista_filtrada = list(filter(lambda n: n<0, lista_original))
print("Lista Filtrada: ")
print(lista_filtrada)