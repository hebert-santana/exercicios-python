# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.

num = int(input("Digite um número inteiro: "))

# criando uma lista com todos inteiros menores que num
lista_numeros = [i for i in range(1, num)]
lista_divisores = []

# verifica se na lista há algum divisor de num
for numeros in lista_numeros:
    if num % numeros == 0:
        lista_divisores.append(numeros)
        
if lista_divisores == []:
    print(f'{num} é primo.')
else:
    print(f'{num} não é primo.\nEle é divisível por: ')
    print(f'{lista_divisores} e por ele mesmo.')
        


        
