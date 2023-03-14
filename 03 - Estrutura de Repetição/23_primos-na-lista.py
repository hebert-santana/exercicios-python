# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. 
# O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. 
# Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

num = int(input("Digite um número inteiro: "))
num_mais = num + 1

# lista com os número de 1 até N
lista_numeros = [i for i in range(1, num_mais)]

# lista de divisores e lista de números primos
lista_primos = []
lista_nao_primos = []

for i in lista_numeros:
    lista_divisores = []
    # criando lista com números de 1 até i
    lista_numeros_numeros = [i for i in range(1, i+1)]
    
    for j in lista_numeros_numeros:
        if i % j == 0:
            lista_divisores.append(j)
            
    if lista_divisores == [1, i] or lista_divisores == [1]:
        lista_primos.append(i)
    else:
        lista_nao_primos.append(i)
 
print(f'Primos: {lista_primos}.\nNão Primos: {lista_nao_primos}.') 