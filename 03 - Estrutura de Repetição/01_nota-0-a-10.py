# Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

while True:
    nota = float(input("Digite uma nota1 entre 0 e 10: "))
    if nota <= 10 and nota >= 0:
        print(f'A nota é: {nota}')
        break
    else:
        print(f'A nota "{nota}" não é valida.')
        print('Informe uma nota válida entre 0 e 10.')
        

