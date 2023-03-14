# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

n_esimo = int(input("Deseja a série com quantos números? "))

def fibonacci(num_elementos):
    n = 1
    lista = [1]
    indice = 1
    # enquanto o tamanho da lista for menor que a quantidade que queremos de elementos
    while len(lista) < num_elementos:
        lista.append(n)
        # n é ele mesmo mais o elemento anterior da lista
        n = n + lista[(indice - 1)]
        # próximo índice
        indice = indice + 1
        
    return lista
        
lista_fibo = fibonacci(n_esimo)

print(lista_fibo)
        
        
    
    