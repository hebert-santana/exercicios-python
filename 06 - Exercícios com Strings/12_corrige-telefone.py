# Valida e corrige número de telefone. 
# Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. 
# O usuário pode informar o número com ou sem o traço separador.
# Telefone corrigido sem formatação: 34610133
# Telefone corrigido com formatação: 3461-0133

separador = '-'
original = input('Digite o número do telefone: ').strip()[-9:]
num_telefone = original

# adiciona o prefixo 3 se necessário
if len(num_telefone) == 7 and num_telefone.isnumeric():
    num_telefone = '3' + num_telefone
elif len(num_telefone) == 8 and num_telefone[3] == separador:
    num_telefone = '3' + num_telefone[:3] + num_telefone[4:]

# adiciona o separador se necessário
if separador not in num_telefone:
    num_telefone = num_telefone[:4] + separador + num_telefone[4:]

print(f'Telefone corrigido sem formatação: {original}')
print(f'Telefone corrigido com formatação: {num_telefone}')
