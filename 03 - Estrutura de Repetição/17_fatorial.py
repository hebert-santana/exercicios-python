# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

num = int(input("Número: "))

n = 0
fatorial = 1

while n < num:
    n = n + 1
    fatorial = fatorial * n

print(fatorial)  