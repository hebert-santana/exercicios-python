# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
"""Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
a. comprar apenas latas de 18 litros;
b. comprar apenas galões de 3,6 litros;
c. misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias."""

import math

# Área para pintar
metros = float(input("Digite a área total (m²): "))

# Quantidade de litros tinta única
qntd_litros = math.ceil(metros / 6)
# Quantidade de latas únicas
qntd_a = math.ceil(qntd_litros / 18)
qntd_b = math.ceil(qntd_litros / 3.6)
# Valor latas únicas
valor1 = qntd_a * 80
valor2 = qntd_b * 25

print("a. Comprar ", qntd_a, " latas de 18 litros. O valor total da compra é: R$", valor1)
print("b. Comprar ", qntd_b, " latas de 3,6 litros. O valor total da compra é: R$", valor2)



# Quantidade de litros misturando latas
qntd_litros_mistura = math.ceil(metros / 6)*1.1

# Função para obter quantidade de latas no caso de misturas (qntd_litros_mistura)
def tintas(litros):
    a = 0
    b = 0
    if litros < 3.6:
        return print("Comprar uma lata de 3,6L. O valor total da compra é: R$ 25")
    elif litros > 3.6 and litros < 18:
        return print("Comprar uma lata de 18L. O valor total da compra é: R$ 80")
    else:
        while (a < (litros/18 - 1)):
            a = a + 1
        else:
            litros = litros - 18*a
            while (b < (litros/3.6)):
                b = b + 1
    valor = 80+a + 25*b
    return(print("c. Comprar ", a, "latas de 18L e ", b, " latas de 3,6L. O valor é: R$", valor))

tintas(qntd_litros_mistura)
