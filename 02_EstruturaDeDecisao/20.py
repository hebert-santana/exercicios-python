# Faça um Programa para leitura de três notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e presentar:
# a. A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# b. A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# c. A mensagem "Aprovado com Distinção", se a média for igual a 10.

num1 = float(input("Forneça a primeira nota: "))
num2 = float(input("Forneça a segunda nota: "))
num3 = float(input("Forneça a terceira nota: "))

def aprovado(x, y, z):
    nota_media = (x+y+z)/3
    if nota_media == 10:
        print("Aprovado com Distinção! Sua média foi: {media}" .format(media = nota_media))
    elif nota_media >= 7:
        print("Aprovado! Sua média foi: {media}" .format(media = nota_media))
    else:
        print("Reprovado! Sua média foi: {media}" .format(media = nota_media))
    
aprovado(num1, num2, num3)