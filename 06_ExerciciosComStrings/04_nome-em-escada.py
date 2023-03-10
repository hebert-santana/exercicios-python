# Nome na vertical em escada. 
# Modifique o programa anterior de forma a mostrar o nome em formato de escada.

print('========== ======== ==========')
nome = input('Digite seu nome: ').upper()

nome_escada = []

for i in nome:
    nome_escada.append(i)
    print(' ')
    for letra in nome_escada:
        print(letra, end='')
    
    
print('\n========== ======== ==========')