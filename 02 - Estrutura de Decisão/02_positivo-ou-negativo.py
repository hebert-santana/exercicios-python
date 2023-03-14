# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num1 = float(input("Forneça o primeiro número: "))

def posNeg(x):
    if x > 0:
        return print("Positivo.")
    elif x < 0:
        return print("Negativo.")
    else:
        return print("Igual a Zero.")
    
posNeg(num1)