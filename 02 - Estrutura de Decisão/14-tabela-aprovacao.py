# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. 
# A atribuição de conceitos obedece à tabela abaixo:
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

# Função tabulare para imprimir tabela
from tabulate import tabulate

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota1 + nota2) /2

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

conceito_texto, conceito_letra, resultado_aprovado = conceito(media)


tabela = [['Média de Aproveitamento', 'Conceito', 'Resultado'], [conceito_texto, conceito_letra, resultado_aprovado]]
print(tabulate(tabela, headers='firstrow', tablefmt='fancy_grid'))

    