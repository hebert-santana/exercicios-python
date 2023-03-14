# Data por extenso. 
# Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.
print('============= DATA POR EXTENSO =============')
data = input('Data de Nascimento (dd/mm/aaaa): ')

dia = data[:2]
mes = data[3:5]
ano = data[6:]

meses = {'01': 'janeiro', '02': 'fevereiro', '03': 'março', '04': 'abril', '05': 'maio', '06': 'junho', '07': 'julho', '08': 'agosto', '09': 'setembro', '10': 'outubro', '11': 'novembro', '12': 'dezembro'}
mes_extenso = meses[dia]

print(f'Você nasceu em {dia} de {mes_extenso} de {ano}.')

print('========== ====================== ==========')