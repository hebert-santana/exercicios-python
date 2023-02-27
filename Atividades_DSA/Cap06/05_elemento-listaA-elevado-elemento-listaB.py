# Exercício 5 - Abaixo você encontra duas listas. Faça com que cada elemento da listaA seja elevado ao elemento correspondente na listaB.
listaA = [2, 3, 4]
listaB = [10, 11, 12]

# aplicando a função de potência nos elementos das listas
lista_resultado = list(map(lambda a, b: a**b, listaA, listaB))

# imprimindo resultado
print("Resultado: ")
print(lista_resultado)