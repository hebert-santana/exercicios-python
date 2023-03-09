#Faça um programa para imprimir:
#     1
#     2   2
#     3   3   3
#     .....
#     n   n   n   n   n   n  ... n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

numero_n = int(input("Quantas linhas? "))

def geraTriangulo(n):
    i = 0
    linhas =''
    while i <= n:
        linhas += i * (str(i) + ' ') + '\n'
        i += 1
    return linhas

print('========== Gerador de Triângulo Numérico ==========')       
print(geraTriangulo(numero_n))
print('========== ============================= ==========')  
