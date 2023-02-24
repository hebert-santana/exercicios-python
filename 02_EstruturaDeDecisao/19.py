# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

numero = input("Digite um número inteiro de 0 até 999: ")

# verificante quantidade de dígitos
if len(numero) > 3:
    print("Valor inválido! O número deve ser de até 3 dígitos!")
    
 # criando lista vazia   
lista_numeros = []

# criando uma lista com os números e transformando em inteiro
for i in numero:
    i = int(i)
    lista_numeros.append(i)

# verificando tamanho da lista e especificando condições
if len(lista_numeros) == 3:
    print("{0} {1} {2} = {2} centenas, {1} dezenas e {0} unidades." .format(lista_numeros[2], lista_numeros[1], lista_numeros[0]))
elif len(lista_numeros) == 2:
    print("{0} {1} = {1} dezenas e {0} unidades." .format(lista_numeros[1], lista_numeros[0]))
else:
    print("{0} = {0} unidades." .format(lista_numeros[0]))
    
    
        
        