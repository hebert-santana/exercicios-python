# Exercício 4 - Crie duas funções, uma para elevar um número ao quadrado e outra para elevar ao cubo. 
# Aplique as duas funções aos elementos da lista abaixo. 
# Obs: as duas funções devem ser aplicadas simultaneamente.


lista = [0, 1, 2, 3, 4]

# criando as funções
def quadrado(n):
    return n**2

def cubo(n):
    return n**3

# aplicando as funções na lista
lista_resultado = list(map(lambda n: [quadrado(n), cubo(n)], lista))

# imprimindo resultado
print(lista_resultado)



