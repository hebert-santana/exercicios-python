while True:
    entrada = input("Digite um número inteiro: ")
    if entrada.isnumeric():
        numero = int(entrada)
        print(f'Entrada validada: {numero}')
        break
    else:
        print("Entrada inválida. Digite apenas números.")