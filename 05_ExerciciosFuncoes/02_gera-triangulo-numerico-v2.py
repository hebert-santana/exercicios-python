# Faça um programa para imprimir:
#     1
#     1   2
#     1   2   3
#     .....
#     1   2   3   ...  n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
print('========== Gerador de Triângulo Numérico V2 ==========')
numero_n = int(input("Quantas linhas? "))

def geraTriangulo(numero_linhas):
    escada = []
    
    # insere números de 0 a n na lista escada
    n = 0
    while n <= numero_linhas:
        escada.append(n)
        n += 1
    
    # remove o número zero da lista
    escada = escada[1:]
       
    # imprime linha por linha
    caracteres = 0
    while caracteres <= numero_linhas:
        for i in range(caracteres):
            print(escada[i], end=' ')
        # saltar uma linha
        print()
        caracteres += 1

# executando a função      
geraTriangulo(numero_n)
print('========== ================================ ==========') 