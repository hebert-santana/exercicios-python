# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9)

f_temp = float(input("Digite a temperatura (F°): "))

def converte_temp (temp):
    c_temp =  5 * ((temp - 32)/ 9)
    return c_temp

celsius_temperatura = converte_temp(f_temp)

print(f'{f_temp} F° = {celsius_temperatura} C°')