# Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
# Depois modifique o programa para que ele mostre os números um ao lado do outro.

lista_numeros = list(range(1, 21))

for num in lista_numeros:
    print(num)
    
print('\n-----------------------------------------------\n\n')

for num in lista_numeros:
    print(num, end=' ') # em vez de imprimir uma quebra de linha depois de cada elemento, separar por um espaço em branco


