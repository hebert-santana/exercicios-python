# Leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

while True:
    numero = input("Digite um número inteiro de 0 até 999: ").strip()
    # verificante quantidade de dígitos
    if len(numero) > 3 or not numero.isnumeric():
        print("Valor Inválido!")
    else:        
        # criando lista vazia   
        lista_numeros = []
        # criando uma lista com os números e transformando em inteiro
        for i in numero:
            i = int(i)
            lista_numeros.append(i)
        # verificando tamanho da lista e especificando condições
        if len(numero) == 3:
            print(f'{numero} = {lista_numeros[0]} centenas, {lista_numeros[1]} dezenas e {lista_numeros[2]} unidades.')
            break
        elif len(numero) == 2:
            print(f'{numero} = {lista_numeros[0]} dezenas e {lista_numeros[1]} unidades.')
            break
        else:
            print(f'{numero} = {lista_numeros[0]} unidades.')
            break
    
    
        
        