# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.

valor_limite = 500

def fibonacci(limite):
    n = 1
    lista = [1]
    indice = 0
    while lista[indice] < limite:
        lista.append(n)
        indice = indice + 1
        n = n + lista[(indice - 1)]        
    return lista
        
lista_fibo = fibonacci(valor_limite)

print(lista_fibo)
        