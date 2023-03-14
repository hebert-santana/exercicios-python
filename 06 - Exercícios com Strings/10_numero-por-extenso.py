# Número por extenso. 
# Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.
print('===================== NUMERO POR EXTENSO =====================')

num = int(input('Digite um número (de 0 até 99): '))

unidades_ext = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
primeira_dezena_ext = ['dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
demais_dezenas_ext = ['','', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']

if num >= 0 and num <= 9:
    print(f'{num} = {unidades_ext[num]}')
elif num > 9 and num < 20:
    print(f'{num} = {primeira_dezena_ext[num - 10]}')
elif num >= 20 and num <= 99:
    maior_19 = str(num)
    dezena = int(maior_19[0])
    unidade = int(maior_19[1])
    dezena_extenso = demais_dezenas_ext[dezena]
    unidade_extenso = unidades_ext[unidade]
    if unidade_extenso == 'zero':
        print(f'{num} = {dezena_extenso}')
    else:
        print(f'{num} = {dezena_extenso} e {unidade_extenso}')
else:
    print('Número Inválido!')    


print('===================== ================== =====================')