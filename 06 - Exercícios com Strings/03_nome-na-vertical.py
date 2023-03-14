# Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.

print('========== ======== ==========')
nome = input('Digite seu nome: ').upper()

espaco = ' '
conta_espaco = 0
for i in nome:
    total_espacos = espaco * conta_espaco
    print(total_espacos, i)
    conta_espaco += 1
    
print('========== ======== ==========')
    
