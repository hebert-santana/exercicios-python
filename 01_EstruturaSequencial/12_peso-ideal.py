# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

h = float(input("Digite sua altura (m): "))

# cálculo arredondado para duas casas decimais
peso_ideal = round((72.7 * h) - 58, 2)

print(f"Seu peso ideal é: {peso_ideal} Kg.")