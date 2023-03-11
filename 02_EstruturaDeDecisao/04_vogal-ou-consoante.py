# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

# Listas para comparação
lista_vogais = ["A", "E", "I", "O", "U"]
lista_consoantes = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

while True:
    letra = str(input("Digite uma letra: ")).strip().upper()[0]
    if letra in lista_vogais:
        print(f"\033[33m {letra} é vogal.\033[0m")
        break
    elif letra in lista_consoantes:
        print(f"\033[33m {letra} é consoante.\033[0m")
        break

