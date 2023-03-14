# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# a. par ou ímpar;
# b. positivo ou negativo;
# c. inteiro ou decimal.

# resultado da operação
r = 0
# variável de início
par_impar = 'impar'
pos_neg = 'positivo'
int_dec = 'inteiro'
    
while True:
    op = int(input('[1] - Somar \n[2] - Subtrair\nQual operação deseja realizar: '))
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    
    if op == 1:
        r = n1 + n2
    elif op == 2:
        r = n1 - n2
    else:
        print('Operação inválida.')
        break

    if r % 2 == 0:
        par_impar = 'par'
    if r < 0:
        pos_neg = 'negativo'
    if r != int(r):
        int_dec = 'decimal'
    print(f'Resultado = {r}.')
    print(f'{r} é um número {par_impar}, {int_dec} e {pos_neg}.')
    break
    