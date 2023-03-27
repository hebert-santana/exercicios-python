# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
# Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram 
# (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).



print('========== Análise de Temperaturas ==========')
print()

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

# leitura das temperaturas médias de cada mês
temperaturas = []
for i in range(12):
    temperatura = float(input(f'Informe a temperatura média °C de {meses[i]}: '))
    temperaturas.append(temperatura)

# média anual das temperaturas
media_anual = sum(temperaturas) / len(temperaturas)

# imprimindo as temperaturas acima da média anual e seus respectivos meses
print(f'\nTemperaturas acima da média anual ({media_anual:.2f}) °C: ')
for i in range(12):
    if temperaturas[i] > media_anual:
        print(f'{meses[i]}: {temperaturas[i]:.2f} °C')
