# Verificação de CPF. 
# Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx 
# e indique se é um número válido ou inválido através da validação dos dígitos verificadores e dos caracteres de formatação.
print('===================== VALIDA CPF =====================')

cpf = str(input('Informe o CPF (xxx.xxx.xxx-xx ): '))
cpf_numeros = cpf.replace('.', '').replace('-', '')

if len(cpf) != 14:
    print('Formato Inválido!')
elif not cpf_numeros.isnumeric():
    print('Formato Inválido! Campo de Números.')
elif cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-':
    print('Formato Inválido! Campo de Divisores.')
else:
    print('CPF validado.')
    
print('===================== ========== =====================')
