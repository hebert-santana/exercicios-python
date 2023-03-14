# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
print('\033[1;31;43m=============== PESO IDEAL ===============\033[m')
h = float(input("Digite sua altura (m): "))

print("Qual seu gênero?\n[M] - Masculino\n[F] - Feminino")

# validando entrada de gênero
while True:
    genero = input("Gênero: ").strip().upper()[0]
    if genero in 'MF':
        break

if genero == 'M':
    h_peso_ideal = round((72.7 * h) - 58, 2)
    print("Seu peso ideal é: ", h_peso_ideal, " Kg.")
elif genero == 'F':
    m_peso_ideal = round((62.1 * h) - 44.7, 2)
    print("Seu peso ideal é: ", m_peso_ideal, " Kg.")
else:
    print("Erro! Tente novamente.")