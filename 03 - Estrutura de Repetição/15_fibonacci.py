# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa capaz de gerar a série até o n−ésimo termo.

n_esimo = int(input("Fibonacci com quantos termos? "))

# termo (n-1)
n1 = 0
# termo (n-2)
n2 = 0

for i in range(1, n_esimo):
    if n1 + n2 > 0:  
        termo_atual = n1 + n2
        n2 = n1
        n1 = termo_atual
    else:
        n1 += 1
        termo_atual = 1
    print(termo_atual)
    
    
    