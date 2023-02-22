# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

# peso_limite = 50
# multa 4.00 por Kg excedente
# calcular o excesso em Kg

peso = float(input("Forneça o peso (Kg): "))
limite = 50
multa_kg = 4

if peso > limite:
    excesso = round(peso - limite, 2)
    multa = round(multa_kg * excesso, 2)
    print("O peso excedeu em ", excesso, "Kg. Você deve pagar uma multa de R$", multa)
else:
    print("O peso não excedeu o limite.")
