# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

salario_hora = float(input("Quanto você recebe por hora? "))
horas_mes = float(input("Quantas horas você trabalha por mês? "))

salario_total = salario_hora * horas_mes

print(f"Seu salário total nesse mês é: R$ {salario_total}.")