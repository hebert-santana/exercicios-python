# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes 
# e limitando o fatorial a números inteiros positivos e menores que 16.

# Loop para obter uma entrada do usuário
while True:
    num = input("Digite um número entre 0 e 15: ")
    # Verifica se a entrada é um número
    if num.isnumeric():
        valor = int(num)        
        # Verifica se o valor está dentro do intervalo desejado
        if valor >= 0 and valor < 16:
            print(f'Número escolhido: {valor}')
            break
        else:
            print("Valor Inválido!\nO valor deve estar entre 0 e 16.")
    else:
        print("A entrada deve ser um número inteiro. Tente novamente.")

    
n = 0
fatorial = 1

while n < valor:
    n = n + 1
    fatorial = fatorial * n

print(f'Fatorial de {valor} = {fatorial}') 