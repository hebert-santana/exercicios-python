# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# a. A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# b. A mensagem "Reprovado", se a média for menor do que sete;
# c. A mensagem "Aprovado com Distinção", se a média for igual a dez.
while True:
    n1 = float(input("Forneça a primeira nota: "))
    if n1 >= 0 and n1 <= 10:
        n2 = float(input("Forneça a segunda nota: "))
        if n2 >= 0 and n2 <= 10:
            break

def aprovado(x, y):
    nota = (x+y)/2
    if nota == 10:
        return print(f'\033[33mNota: {nota}\nAprovado com Distinção!\033[0m')
    elif nota >= 7 and nota < 10:
        return print(f'\033[33mNota: {nota}\nAprovado!\033[0m')
    else:
        return print(f'\033[33mNota: {nota}\nReprovado!\033[0m')
    
aprovado(n1, n2)