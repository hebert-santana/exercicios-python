# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

c_temp = float(input("Digite a temperatura (C°): "))

def converte_temp (temp):
    f_temp = (9*temp + 160)/5
    return f_temp

print(c_temp, " C° = ", converte_temp(c_temp), " F°")