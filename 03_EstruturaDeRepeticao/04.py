# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

# atribuindo população inicial
populacao_A = 80000
populacao_B = 200000

# taxas de crescimento
tx_A = 1.03
tx_B = 1.015

# tempo em anos (iniciando no 0)
t = 0

while (populacao_A < populacao_B):
    t = t + 1
    populacao_B = populacao_B * tx_B
    populacao_A = populacao_A * tx_A
    
print(f'Anos necessários: {t}\nPopulação A = {populacao_A}\nPopulação B = {populacao_B}.')