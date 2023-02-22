# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite uma letra: ")

# Tranforma letra em maiúscula
letra = letra.upper()

# Listas para comparação
lista_vogais = ["A", "E", "I", "O", "U"]
lista_consoantes = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

# Comparação
if letra in lista_vogais:
    print("É vogal.")
elif letra in lista_consoantes:
    print("É consoante.")
else:
    print("Erro!")

