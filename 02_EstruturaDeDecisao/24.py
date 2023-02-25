# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# a. par ou ímpar;
# b. positivo ou negativo;
# c. inteiro ou decimal.
import sys

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
print("Qual operação deseja realizar: \n 1 - Somar \n 2 - Subtrair")
operacao = int(input("Digite a operação desejada (1 ou 2): "))


def opera (n1, n2, op):
    if op == 1:
        r = n1 + n2
    elif op == 2:
        r = n1 - n2
    else:
        print("A operação não é válida!")
        sys.exit(0)
    return r

resultado = opera(num1, num2, operacao)

def parImpar(n):
    numero = "impar"
    if n % 2 == 0:
        numero = "par"
    return(numero)

def positivoNegativo(n):
    numero = "é positivo"
    if n == 0:
        numero = "é zero"
    elif n < 0:
        numero = "é negativo"
    return numero

def inteiroDecimal(n):
    numero = " é inteiro"
    if n != int(n):
        numero = " é decimal"
    return numero



p_i = parImpar(resultado)
p_n = positivoNegativo(resultado)
i_d = inteiroDecimal(resultado)

print("Resultado: ",resultado, "\n É um número", p_i, p_n, i_d)