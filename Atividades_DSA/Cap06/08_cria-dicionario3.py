# Exercício 8 - Considere os dois dicionários abaixo. 
# Crie um terceiro dicionário com as chaves do dicionário 1 e os valores do dicionário 2.
dict1 = {'a':1,'b':2}
dict2 = {'c':4,'d':5}

# criando uma lista com as chaves de d1 e valores de d2
lista_dict3 = list(zip(dict1, dict2.values()))
# transformando a lista anterior em um dicionário
dict3 = dict(lista_dict3)

# imprimindo o resultado
print("Resultado \n Dicionário 3 =", dict3)