# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';


while True:
    n = input('Digite seu nome: ').strip().upper()
    if len(n) > 3:
        break
    else:
        print('Nome inválido.')
while True:
    i = float(input('Digite sua idade: '))
    if i > 0 and i <= 150:
        break
    else:
        print('Idade inválida.')
while True:
    s = float(input('Digite seu salário: R$ '))
    if s > 0:
        break
    else:
        print( 'Salário inválido.')
while True:        
    sx = input('[M] - Masculino\n[F] - Feminino\nDigite seu sexo: ').strip().upper()[0]
    if sx in 'FM':
        break
    else:
        print('Sexo inválido.')
while True:
    ec = input('[S] - Solteiro\n[C] - Casado\n[V] - Viúvo\n[D] - Divorciado\nDigite seu estado civil: ').strip().upper()[0]
    if ec in 'SCVD':
        break
    else:
        print('Estado civil inválido')


print('\n==================== DADOS VALIDADOS ====================')      
print(f'Nome: {n}')
print(f'Idade: {i} anos')
print(f'Salário: R${s}')
print(f'Sexo: {sx}')
print(f'Estado Civil: {ec}')



    
    
