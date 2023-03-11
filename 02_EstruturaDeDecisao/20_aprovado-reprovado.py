# Faça um Programa para leitura de três notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e presentar:
# a. A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# b. A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# c. A mensagem "Aprovado com Distinção", se a média for igual a 10.
while True:
    n1 = input("Forneça a primeira nota: ").strip()
    n2 = input("Forneça a segunda nota: ").strip()
    n3 = input("Forneça a terceira nota: ").strip()
    lista_notas = []
         
    for entrada in (n1, n2, n3):
        try:
            nota = float(entrada)
            lista_notas.append(nota)
        except ValueError:
            print(f"Entrada '{entrada}' não é válida.")   
    
    if all(x >= 0 and x <= 10 for x in lista_notas):
        media = (lista_notas[0]+lista_notas[1]+lista_notas[2])/3
        if media == 10:
            print(f"Aprovado com Distinção! Sua média foi: {media}")
            break
        elif media >= 7:
            print(f"Aprovado! Sua média foi: {media}")
            break
        else:
            print(f"Reprovado! Sua média foi: {media}")
            break
    else:
        print("\033[31mNotas não validadas!\033[0m")
    