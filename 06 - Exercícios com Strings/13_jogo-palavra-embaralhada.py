# Jogo da palavra embaralhada. 
# Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas. 
# O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. 
# O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.

from random import choice, shuffle

tentativas = 6

# lendo a lista de palavras do arquivo texto
with open('palavras-forca.txt', 'r') as f:
    palavras = [line.strip() for line in f]

# escolhe uma palavra aleatoriamente
palavra = choice(palavras)
letras = list(palavra)
shuffle(letras)
# juntando a lista em uma string
palavra_embaralhada = ''.join(letras)

print(f'A palavra embaralhada é: {palavra_embaralhada}')

while True:
    palpite = input('Digite o nome: ').lower().strip()
    if palpite == palavra:
        print(f'Acertou, o nome é: {palavra}')
        break
    else:
        tentativas -= 1
        if tentativas > 0:
            print(f'Errou. Resta {tentativas} tentativas.')
        else:
            print('GAME OVER')
            break

