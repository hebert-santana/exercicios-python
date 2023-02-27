# Exercício 1 - Crie uma lista de 3 elementos e calcule a terceira potência de cada elemento.
import random

# lista de palavras
lista_numeros = []

# selecionando 3 números aleatórios entre 1 e 100
for i in range(3):
    numero_aleatorio = random.randint(1, 100)
    lista_numeros.append(numero_aleatorio)

# função para elevar a potência 3    
def potencia(x):
    return x ** 3

# map para aplicar função potencia a cada elemento da lista
lista_ao_cubo = list(map(potencia, lista_numeros))

# imprimindo resultado
print("Lista original: ", lista_numeros)
print("Lista ao cubo: ", lista_ao_cubo)