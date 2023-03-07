# Altere o programa de cálculo dos números primos, 
# informando, caso o número não seja primo, por quais número ele é divisível.

num = int(input("Digite um número inteiro: "))

lista_numeros = [i for i in range(1, num)]
lista_divisores = []

for numeros in lista_numeros:
    if num % numeros == 0:
        lista_divisores.append(numeros)
        
if lista_divisores == []:
    print(f'{num} é primo.')
else:
    print(f'{num} não é primo.\nEle é divisível por: ')
    print(f'{lista_divisores} e por ele mesmo.')