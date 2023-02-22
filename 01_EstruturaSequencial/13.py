# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

h = float(input("Digite sua altura (m): "))
print("Qual seu gênero?")
genero = int(input("Digite 1 se M; digite 2 se F: "))

if genero == 1:
    h_peso_ideal = round((72.7 * h) - 58, 2)
    print("Seu peso ideal é: ", h_peso_ideal, " Kg.")
elif genero == 2:
    m_peso_ideal = round((62.1 * h) - 44.7, 2)
    print("Seu peso ideal é: ", m_peso_ideal, " Kg.")
else:
    print("Erro! Tente novamente.")