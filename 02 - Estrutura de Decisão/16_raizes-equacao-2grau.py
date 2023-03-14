# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#
# a. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve pedir os demais valores, sendo encerrado;
# b. Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# d. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
print('\033[33m==================== CALCULA RAÍZES ====================\033[0m')
import math
import time
import sys

while True:
   a = float(input("Digite a constante 'a': "))
   if a == 0:
      print('A equação não é do segundo grau.')
      time.sleep(1) # aguardar 1 segundo
      sys.exit() # sair da execução
   else:
      b = float(input("Digite a constante 'b': "))
      c = float(input("Digite a constante 'c': "))
      break

# cálculo delta Δ = b²-4ac
Δ = (b**2 - 4*a*c)

# condição de delta
def condicao(delta):
    if delta < 0:
       print("A equação não possui raízes reais! \n Δ < 0")
       time.sleep(1)
       sys.exit()
    elif delta == 0:
       print(f"A equação {a}x²{b}x = -{c} possui apenas uma raíz real. \n Δ = 0")
    else:
       print(f"A equação {a}x²{b}x = -{c} possuio duas raízes reais! \n Δ > 0")

# executa função de condição
condicao(Δ)

# Fase 2: Bhaskara
# raízes
x1 = (-b - math.sqrt(Δ)) / (2*a)
x2 = (-b + math.sqrt(Δ)) / (2*a)

if x1 == x2:
   print(f'A raíz da equação é: {x1}')
else:
   print(f'As raízes da equação são: x1 = {x1} e x2 = {x2}')

print('\033[33m==================== ============== ====================\033[0m')
