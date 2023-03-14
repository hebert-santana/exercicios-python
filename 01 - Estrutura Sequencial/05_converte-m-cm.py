# Faça um Programa que converta metros para centímetros.

# inserindo a medida em metros
medida_m = float(input("Forneça a medida em metros: "))  

# função para fazer a conversão
def conversao(a):
    medida_cm = round(a * 100)
    return medida_cm

# aplicando a função
medida_cm = conversao(medida_m)

# imprimindo o resultado
print(f'{medida_m} é igual a {medida_cm} centímetros.')