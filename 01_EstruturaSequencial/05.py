# Faça um Programa que converta metros para centímetros.

medida_m = float(input("Forneça a medida em metros: "))

def conversao(a):
    medida_cm = round(a * 100)
    return medida_cm

print(medida_m, " metros = ", conversao(medida_m), " centímetros.")