# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
# Valide a entrada e permita repetir a operação.

import sys

# atribuindo população inicial
populacao_A = int(input("População A: "))
populacao_B = int(input("População B: "))

# taxas de crescimento
tx_A = float(input("Taxa crescimento A: "))
tx_B = float(input("Taxa crescimento B: "))

def valida(p1, p2, tx1, tx2):
    t = 0
    if p1 > 0 and p2 > 0 and p1 < p2 and tx1 > 0 and tx2 > 0 and tx1 > tx2:
        while (p1 < p2):
           t = t + 1
           p2 = p2 * tx2
           p1 = p1 * tx1
    else:
        print("Dados não validados!")
        sys.exit()
    return t, int(p1), int(p2)
        
t, populacao_A, populacao_B = valida(populacao_A, populacao_B, tx_A, tx_B)

print(f'Anos necessários: {t}\nPopulação A = {populacao_A}\nPopulação B = {populacao_B}.')



    
