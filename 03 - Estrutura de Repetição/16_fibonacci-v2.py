# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa que gere a série até que o valor seja maior que 500.

limite = 500

# termo (n-1)
n1 = 0
# termo (n-2)
n2 = 0
# termo atual da sequência
termo_atual = 0

while termo_atual < 500:
    if n1 + n2 > 0:  
        termo_atual = n1 + n2
        n2 = n1
        n1 = termo_atual
    else:
        n1 += 1
        termo_atual = 1
    print(termo_atual)
        