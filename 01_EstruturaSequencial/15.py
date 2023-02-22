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


salario_hora = float(input("Quanto você recebe por hora? "))
horas_mes = float(input("Quantas horas você trabalha por mês? "))

salario_bruto = salario_hora * horas_mes
inss = round(salario_bruto * 0.08, 2)
sind = round(salario_bruto * 0.05, 2)
ir = round(salario_bruto * 0.11, 2)
salario_liquido = salario_bruto - inss - sind - ir
    

print("Salário Bruto: R$ ", salario_bruto)
print("IR (11%): R$ ", ir)
print("INSS (8%): R$ ", inss)
print("Sindicato (5%): R$ ", sind)
print("Salário Líquido: R$ ", salario_liquido)
