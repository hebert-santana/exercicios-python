# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. 
# A atribuição de conceitos obedece à tabela abaixo:
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

num1 = float(input("Nota1: "))
num2 = float(input("Nota2: "))

media = (num1 + num2) /2

def conceito(n):
    if media >= 9:
        conceito = "A"
        conceito_str = "Entre 9.0 e 10.0"
        resultado = "Aprovado!"
    elif media >= 7.5:
        conceito = "B"
        conceito_str = "Entre 7.5 e 9.0"
        resultado = "Aprovado!"
    elif media >= 6:
        conceito = "C"
        conceito_str = "Entre 6.0 e 7.5"
        resultado = "Aprovado!"
    elif media >= 4:
        conceito = "D"
        conceito_str = "Entre 4.0 e 6.0"
        resultado = "Reprovado!"
    elif media >= 0:
        conceito = "E"
        conceito_str = "Entre 4.0 e 6.0"
        resultado = "Reprovado!"
    else:
        return print("Valor Inválido!")
    return conceito_str, conceito, resultado

lista = list(conceito(media))

# Função tabulare para imprimir tabela
from tabulate import tabulate

table = [['Média de Aproveitamento', 'Conceito', 'Resultado'], [lista[0], lista[1], lista[2]]]
print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

    