# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
"""Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
a. comprar apenas latas de 18 litros;
b. comprar apenas galões de 3,6 litros;
c. misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias."""
print('\n\033[93m=============== COMPRA DE TINTAS ===============\033[0m')

import math
# Galão A: Galão de 18L custa 80
litros_a = 18
preco_a = 80
# Galão B: Galão de 3,6L custa 25
litros_b = 3.6
preco_b = 25

# inserindo a área a ser pintada pintar
metros = float(input("Digite a área total (m²): "))
# cada litro de tinta cobre um área de 6 metros
litros = math.ceil(metros / 6)
# quantidade de litros misturando latas com folga de 10%
litros_mistura = litros * 1.1

# função para obter quantidade de latas e o preço da compra no caso de tinta única
def tinta_unica(litros_por_galao):
    if litros_por_galao == litros_a:
        latas = math.ceil(litros / 18)
        preco = latas * 80
        return(latas, preco)
    elif litros_por_galao == litros_b:
        latas = math.ceil(litros / 3.6)
        preco = latas * 25
        return(latas, preco)

# quantidade de latas e valor na compra de galões somente de 18L
qnt_latas_A, preco_total_A = tinta_unica(litros_a)
# quantidade de latas e valor na compra de galões somente de 3.6L
qnt_latas_B, preco_total_B = tinta_unica(litros_b)

# imprimindo o resultado usando galões únicos
print(f'a. Comprar {qnt_latas_A} latas de 18L. Preço = R$ {preco_total_A}.' )
print(f'b. Comprar {qnt_latas_B} latas de 3.6L. Preço = R$ {preco_total_B}.' )

# def tintas_mistura(litros):
#     latas_a = math.ceil(litros / 18)
#     # verificar se é possível usar latas de tinta B para completar
#     sobra_a = latas_a * 18 - litros
#     latas_b = math.ceil(sobra_a / 3.6)
#     # calcular o preço total
#     preco_total = latas_a * preco_a + latas_b * preco_b
#     # exibir as informações sobre as tintas misturadas
#     print(f"c. Tintas Misturadas:")
#     print(f"  Comprar {latas_a} lata(s) de 18L e {latas_b} lata(s) de 3.6L.")
#     print(f"  Preço Total = R$ {preco_total}.")
    
# função para obter quantidade de latas e o preço da compra no caso de misturas das latas
def tinta_mistura(litros):
    # comprar o máximo de tintas A até faltar menos de 18L de tintas e então avaliar o caso.
    # caso precise de até 10.8L
    if litros/1.1 <= 10.8:
        return print("Comprar uma lata de 3,6L. Preço = R$ 25.")
    # caso precise de mais de 10,8L até 18L
    elif litros/1.1 > 10.8 and litros/1.1 <= 18:
        return print("Comprar uma lata de 18L. Preço = R$ 80.")
    # se precisar de mais de 18L
    else:
        # só vale a pena comprar até máximo 3 latas do tipo B (10,8L = R$ 75) que é 60% de litros uma lata do tipo A
        # comprar o máximo de latas do tipo A até que a diferença entre litros comprados e litros faltantes seja no máximo 10,8L
        qnt_A = litros / litros_a
        latas_para_comprar_A = math.floor(qnt_A)            
        # avaliar a quantidade de litros que falta comprar
        diferenca_restante = qnt_A - latas_para_comprar_A
        if diferenca_restante > 0.6:
            # comprar só latas A
            latas_para_comprar_A = math.ceil(qnt_A)
            preco = latas_para_comprar_A * 80
            return print(f"c. Tintas Misturadas:\n  Comprar {latas_para_comprar_A} lata de 18L. Preço = R$ {preco}.")
        elif diferenca_restante <= 0.6 and diferenca_restante > 0.4:
            # comprar 3 latas B
            latas_para_comprar_B = 3
            preco = latas_para_comprar_A * 80 + latas_para_comprar_B * 25
            return print(f"c. Tintas Misturadas:\n  Comprar {latas_para_comprar_A} lata de 18L.\n  Comprar {latas_para_comprar_B} latas de 3.6L.\n  Preço Total = R$ {preco}.")
        elif diferenca_restante <= 0.4 and diferenca_restante > 0.2:
            # comprar 2 latas B
            latas_para_comprar_B = 2
            preco = latas_para_comprar_A * 80 + latas_para_comprar_B * 25
            return print(f"c. Tintas Misturadas:\n  Comprar {latas_para_comprar_A} lata de 18L.\n  Comprar {latas_para_comprar_B} latas de 3.6L.\n  Preço Total = R$ {preco}.")
        else:
            # comprar 1 latas B
            latas_para_comprar_B = 1
            preco = latas_para_comprar_A * 80 + latas_para_comprar_B * 25
            return print(f"c. Tintas Misturadas:\n  Comprar {latas_para_comprar_A} lata de 18L.\n  Comprar {latas_para_comprar_B} latas de 3.6L.\n  Preço Total = R$ {preco}.")
        
tinta_mistura(litros_mistura)
            
print('\n\033[93m=============== ================ ===============\033[0m')

