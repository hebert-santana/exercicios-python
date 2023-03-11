# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são:

# a. X% IR - depende do salário bruto 
# b. 3% Sindicato 
# c. 11% FGTS - não é descontado (é a empresa que deposita).
# d. 10% INSS

# O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# 
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% 
# 
# Imprima na tela as informações, dispostas conforme o exemplo. 
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.
print(f"\033[33m========================== CALCULA SALÁRIO ==========================\033[0m")

valor_hora = float(input("Valor da hora trabalhada: "))
horas_mes = float(input("Total de horas trabalhadas no mês: "))

# cálculo salário bruto
salario_b = valor_hora * horas_mes

# descontos que não variam o porcentual
inss = salario_b * 0.1
sindicato = salario_b * 0.03
fgts = salario_b * 0.11

# função para aplicar o desconto do IR
def descontoIR(salario):
    if salario > 2500:
        ir = salario * 0.2
    elif salario > 1500:
        ir = salario * 0.1
    elif salario > 900:
        ir = salario * 0.05
    elif salario <= 900 and salario > 0:
        ir = 0
    else:
        return print("Valor IR Inválido!")
    return ir

# cálculo salário líquido 
total_descontos = inss + sindicato + descontoIR(salario_b)
salario_liquido = salario_b - total_descontos

# Impressão resultado
print(f'Salário Bruto: R${salario_b}\n (-) IR: R${descontoIR(salario_b)}\n (-) INSS: R${inss}\n (-) Sindicato: R${sindicato}\n FGTS: R${fgts}\n Total Descontos: R${total_descontos}\n Salário Líquido: R${salario_liquido}')

print(f"\033[33m========================== =============== ==========================\033[0m")
