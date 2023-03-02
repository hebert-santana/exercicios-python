# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

# importando o módulo math para acessar função pi
import math

# solicitando o raio
r = float(input("Digite o raio do círculo: "))

# calculando a área do círculo
area = math.pow(r, 2) * math.pi

# imprimindo o resultado
print(f'A área do círculo é: {area}.')