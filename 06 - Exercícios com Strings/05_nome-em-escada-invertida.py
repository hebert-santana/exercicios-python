# Nome na vertical em escada invertida. 
# Altere o programa anterior de modo que a escada seja invertida.

print('========== ======== ==========')
nome = input('Digite seu nome: ').upper()

nome_escada = []

# insere as strings do nome na lista
for i in nome:
    nome_escada.append(i)

tamanho_nome = len(nome_escada)

i = 0
while i < tamanho_nome:
    # transforma lista em string e imprime
    nome = ' '.join(nome_escada)
    print(nome)
    # remove o último caractere
    nome_escada.pop(-1)
    i += 1
    
    
    
    
print('========== ======== ==========')