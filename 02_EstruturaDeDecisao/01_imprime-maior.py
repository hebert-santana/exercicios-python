# Faça um Programa que peça dois números e imprima o maior deles.

num1 = float(input("Forneça o primeiro número: "))
num2 = float(input("Forneça o segundo número: "))

def funcaoCompara(x, y):
    if x > y:
        return print(x)
    elif y > x:
        return print(y)
    else:
        return print("São iguais!")
    
funcaoCompara(num1, num2)