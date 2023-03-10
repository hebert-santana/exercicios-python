# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

c_temp = float(input("Digite a temperatura (C°): "))

def converte_temp (temp):
    f_temp = (9*temp + 160)/5
    return f_temp

fahrenheit_temperatura = converte_temp(c_temp)

print(f'{c_temp} C° = {fahrenheit_temperatura} F°')