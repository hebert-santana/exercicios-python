# Palíndromo. 
# Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. 
# 
# Por exemplo: OSSO e OVO são palíndromos. 
# Em textos mais complexos os espaços e pontuação são ignorados.

# A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. 
# Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.

print('===================== DETECTA PALÍNDROMO =====================')
string = str(input('Palavra ou frase: ')).upper()

# removendo espaços vazios
string_limpa = string.replace(' ', '')

# transformando em uma lista
lista_string = list(string_limpa)

# cria uma lista com elementos da lista anterior invertidos
lista_string_inv = lista_string.copy()
lista_string_inv.reverse()

# compara as listas; se iguais, é palíndromo
if lista_string == lista_string_inv:
    print(f'{string} é um Palíndromo.')
else:
    print(f'{string} não é um Palíndromo.')

print('===================== ================== =====================')