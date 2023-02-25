# Faça um Programa para um caixa eletrônico. 
# O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
# O valor mínimo é de 10 reais e o máximo de 600 reais. 
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.

# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

valor_saque = int(input("Qual valor deseja sacar? (mínimo R$10 / máximo 600) "))

import sys

# verificante quantidade de dígitos
if valor_saque > 600 or valor_saque < 10:
    print("Valor inválido! \n Valor Mínimo: R$ 10 \n Valor Máximo: 600")
    sys.exit(0)

# criando lista vazia
lista_saque = []   
# transformando número em str e depois em lista
lista_saque_str = list(str(valor_saque))
print(lista_saque_str)
# criando uma lista com os números e transformando em inteiro
for i in lista_saque_str:
    i = int(i)
    lista_saque.append(i)
    
print(lista_saque)

# atribuindo valores da lista à variáveis
nota_100 = lista_saque[0]

if lista_saque[1] > 4:
    nota_50 = 1
    nota_10 = lista_saque[1] - 5
else:
    nota_10 = lista_saque[1]
    
if lista_saque[2] > 4:
    nota_5 = 1
    nota_1 = lista_saque[2] - 5
else:
    nota_1 = lista_saque[2]

# imprimindo resultado
print("Para sacar R$", valor_saque, "forneceremos: \n", nota_100, " notas de 100 \n", nota_50, " notas de 50 \n", nota_10, " notas de 10 \n", nota_5, " notas de 5 \n", nota_1, " notas de 1")