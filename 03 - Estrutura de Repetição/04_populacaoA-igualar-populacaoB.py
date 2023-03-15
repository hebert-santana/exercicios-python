# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 
# 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país 
# A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

# população inicial
pop_A = 80000
pop_B = 200000

# taxas de crescimento
tx_A = 1.03
tx_B = 1.015

# tempo em anos (iniciando no 0)
t = 0

while (pop_A < pop_B):
    t = t + 1
    pop_B = pop_B * tx_B
    pop_A = pop_A * tx_A
    
print(f'Anos necessários: {t}\nPopulação A = {pop_A}\nPopulação B = {pop_B}.')