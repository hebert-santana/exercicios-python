# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# a. salário bruto.
# b. quanto pagou ao INSS.
# c. quanto pagou ao sindicato.
# d. o salário líquido.
# e. calcule os descontos e o salário líquido, conforme a tabela abaixo:

# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

s = float(input("Quanto você recebe por hora? "))
h = float(input("Quantas horas você trabalha por mês? "))

bruto = s * h
inss = round(bruto * 0.08, 2)
sind = round(bruto * 0.05, 2)
ir = round(bruto * 0.11, 2)
salario_liquido = bruto - inss - sind - ir
    
print('\n\033[93m=============== INFORMAÇÕES DO SALÁRIO ===============\033[0m')
print("\033[92mSalário Bruto: R$\033[0m", bruto)
print("\033[92mIR (11%): R$\033[0m", ir)
print("\033[92mINSS (8%): R$\033[0m", inss)
print("\033[92mSindicato (5%): R$\033[0m", sind)
print("\033[92mSalário Líquido: R$\033[0m", salario_liquido)
print('\033[93m=============== ====================== ===============\033[0m')
