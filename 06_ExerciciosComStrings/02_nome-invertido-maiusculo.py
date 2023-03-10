# Nome ao contrário em maiúsculas. 
# Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. 
# Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.
print('===== ============== =====')
nome = input('Digite seu nome: ').upper()

lista_nome = []
for i in nome:
    lista_nome.append(i)
    
lista_nome.reverse()

print('===== NOME INVERTIDO =====')
for i in lista_nome:
    print(i, end='')
    
print('\n===== ============== =====')