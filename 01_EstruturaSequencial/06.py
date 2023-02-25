# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

# importando o módulo math para acessar função pi
import math

r = float(input("Digite o raio do círculo: "))
area = math.pow(r, 2) * math.pi

print("A área do círculo é: ", area)