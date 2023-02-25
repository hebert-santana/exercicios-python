# Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

num = int(input("Digite um número: "))

def parImpar(n):
    numero = "impar"
    if n % 2 == 0:
        numero = "par"
    return(numero)

print("O número", num, "é", parImpar(num))