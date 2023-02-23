# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#
# a. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve pedir os demais valores, sendo encerrado;
# b. Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# d. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

import math
import sys
a = float(input("Digite a constante 'a': "))

# importando sys para encerrar programa
# encerrando se condição for atendida
if a == 0:
    sys.exit(0)

b = float(input("Digite a constante 'b': "))
c = float(input("Digite a constante 'c': "))

# cálculo delta
delta = (b**2 - 4*a*c)

# condição de delta


def condicao(d):
    if d < 0:
       return print("A equação não possui raízes reais! \n Δ < 0"), sys.exit(0)
    elif d == 0:
       return print("A equação possui apenas uma raíz real. \n Δ = 0")
    else:
       return print("A equação possuio duas raízes reais! \n Δ > 0")

condicao(delta)

# Fase 2: Bhaskara

# importando math para realizar função raíz quadrada

# raízes
x1 = (-b - math.sqrt(delta)) / (2*a)
x2 = (-b + math.sqrt(delta)) / (2*a)

print("As raízes da equação são: x1 = ", x1, " x2 = ", x2)
