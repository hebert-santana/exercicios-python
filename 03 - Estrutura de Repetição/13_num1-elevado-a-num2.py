# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. 
# Não utilize a função de potência da linguagem

num1 = float(input("Base: "))
num2 = float(input("Expoente: "))
resultado = num1 ** num2
print(f'{num1} elevado a {num2} = {resultado}')