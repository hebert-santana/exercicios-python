# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

print("Referência Número/Dia da Semana: \n 1 - Domingo \n 2 - Segunda \n 3 - Terça \n Etc...")
num_dia = int(input("Digite o número referente ao dia da semana: "))

# lista com números válidos
numeros_validos = [1, 2, 3, 4, 5, 6, 7]

# dicionário com pares número: dia da semana
dicionario_dias = {1: "Domingo",
                   2: "Segunda",
                   3: "Terça",
                   4: "Quarta",
                   5: "Quinta",
                   6: "Sexta",
                   7: "Sábado"}

if num_dia in numeros_validos:
    print("O dia da semana é: ", dicionario_dias.get(num_dia))
else:
    print("Valor Inválido!")