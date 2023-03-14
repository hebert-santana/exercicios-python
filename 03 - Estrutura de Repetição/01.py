# Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = int(input("Digite um valor inteiro entre 0 e 10: "))

if nota > 10 or nota < 0:
    while nota < 0 or nota > 10:
        print("Valor Inválido!")
        nota = int(input("Digite um valor inteiro entre 0 e 10: "))
        
print("A nota de valor", nota, "foi validada.")
        

