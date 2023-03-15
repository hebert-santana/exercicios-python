# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. 
# O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. 
# Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

n = int(input("Digite um número inteiro: "))

# lista com os número de 1 até N
lista_numeros = [i for i in range(1, (n+1))]

# lista de divisores e lista de números primos
primos = []
nao_primos = []

for i in lista_numeros:
    lista_divisores = []
    # criando lista com números de 1 até i
    lista_numeros_i = [i for i in range(1, (i+1))]
    
    for j in lista_numeros_i:
        if i % j == 0:
            lista_divisores.append(j)
            
    if lista_divisores == [1, i] or lista_divisores == [1]:
        primos.append(i)
    else:
        nao_primos.append(i)
 
print(f'Primos: {primos}.\nNão Primos: {nao_primos}.') 