# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
# Valide a entrada e permita repetir a operação.

while True:
# atribuindo população inicial
    pop_A = int(input("População A: "))
    pop_B = int(input("População B: "))

# taxas de crescimento
    tx_A = float(input("Taxa crescimento A: "))
    tx_B = float(input("Taxa crescimento B: "))

# tempo
    t = 0
    
    while (pop_A < pop_B):
        t = t + 1
        pop_B = pop_B * tx_B
        pop_A = pop_A * tx_A
        
    print(f'Anos necessários: {t}\nPopulação A = {pop_A}\nPopulação B = {pop_B}.')
    
    repetir = input('\n[S] - SIM\n[N] - Não\nDeseja repetir a operação?').strip().upper()[0]
    if repetir == 'N':
        break



    
