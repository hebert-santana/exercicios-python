# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

# importando math para usar função ceil()
import math

# inserindo a área a ser pintada
metros = float(input("Digite a área total (m²): "))

# calculando a quantidade de litros, número de latas e o valor
def calculo(area):
    litros = math.ceil(area / 3)
    latas = math.ceil(litros / 18)
    preco = latas * 80
    return (latas, preco)

numero_latas, preco_total = calculo(metros)

print(f'Você deve comprar {numero_latas} latas de tinta.\nSua compra fica em R$ {preco_total}.')