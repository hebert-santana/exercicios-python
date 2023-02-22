# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# a. A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# b. A mensagem "Reprovado", se a média for menor do que sete;
# c. A mensagem "Aprovado com Distinção", se a média for igual a dez.

num1 = float(input("Forneça a primeira nota: "))
num2 = float(input("Forneça a segunda nota: "))

def aprovado(x, y):
    nota_media = (x+y)/2
    if nota_media == 10:
        return print("Aprovado com Distinção!")
    elif nota_media >= 7 and nota_media < 10:
        return print("Aprovado!")
    elif nota_media < 7:
        return print("Reprovado!")
    else:
        return print("Erro!")
    
aprovado(num1, num2)