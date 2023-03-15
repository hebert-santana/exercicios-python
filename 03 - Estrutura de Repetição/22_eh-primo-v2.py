# Altere o programa de cálculo dos números primos, 
# informando, caso o número não seja primo, por quais número ele é divisível.

num = int(input("Digite um número inteiro: "))

# criando uma lista com todos inteiros menores que num
inteiros = [i for i in range(1, num)]
lista_divisores = []
divisores_primo = [1, num]
# verifica se na lista há algum divisor de num
for n in inteiros:
    if num % n == 0:
        lista_divisores.append(n)
        
if lista_divisores == divisores_primo:
    print(f'{num} é primo.')
else:
    print(f'{num} não é primo.\nEle é divisível por: ')
    print(f'{lista_divisores} e por ele mesmo.')