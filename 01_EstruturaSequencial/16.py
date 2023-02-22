# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

# importando math para usar função ceil()
import math

metros = float(input("Digite a área total (m²): "))

qntd_litros = math.ceil(metros / 3)
qntd_latas = math.ceil(qntd_litros / 18)
valor = qntd_latas * 80

print("Amigo usuário, você deve comprar ", qntd_latas, " latas. O valor total da compra é: R$", valor)