# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a. o produto do dobro do primeiro com metade do segundo .
# b. a soma do triplo do primeiro com o terceiro.
# c. o terceiro elevado ao cubo.

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite um número inteiro: "))
num3 = float(input("Digite um número real: "))

def funcao_a(n1, n2):
    resultado = (n1 * 2) * (n2 / 2)
    return resultado

def funcao_b(n1, n2):
    resultado = (n1 * 3) + n2
    return resultado

def funcao_c(n1):
    resultado = n1**3
    return resultado

print("Resposta letra a: ", funcao_a(num1, num2))
print("Resposta letra b: ", funcao_b(num1, num3))
print("Resposta letra c: ", funcao_c(num3))