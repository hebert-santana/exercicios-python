# função try-except para tratar exceções caso a conversão para float falhe
while True:
    entrada = input("Digite um número inteiro ou decimal: ")
    try:
        numero = float(entrada)
        if numero.is_integer():
            numero = int(numero)
            print(f'Entrada validada: {numero}')
        else:
            print(f'Entrada validada: {numero}')
        break
    except ValueError:
        print("Entrada inválida. Digite apenas números.")