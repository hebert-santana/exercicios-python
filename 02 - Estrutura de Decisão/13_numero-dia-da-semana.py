# Faça um Programa que leia um número e exiba o dia correspondente da semana. 
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

print('=======================================================================')
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

while True:
    print("Referência número/dia da Semana:\n 1 - Domingo\n 2 - Segunda\n 3 - Terça\n 4 - Quarta\n 5 - Quinta\n 6 - Sexta\n 7 - Sábado")
    num_dia = int(input("Digite o número do dia da semana: "))
    if num_dia in numeros_validos:
        print("\033[33mO dia da semana é: \033[0m", dicionario_dias.get(num_dia))
        break
    else:
        print('\033[31mValor Inválido!\033[0m')
    
print('=======================================================================')