# Jogo de Forca. Desenvolva um jogo da forca. 
# O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. 
# O jogador poderá errar 6 vezes antes de ser enforcado.

from random import choice

# lendo a lista de palavras do arquivo texto
with open('palavras-forca.txt', 'r') as f:
    palavras = [line.strip() for line in f]

# escolhe uma palavra aleatoriamente
palavra_secreta = choice(palavras)

# inicializa a lista de letras já adivinhadas como vazia
letras_adivinhadas = []

# define o numero maximo de tentativas
tentativas = 6

while True:
    # imprime o estado atual da palavra secreta
    palavra_atual = ''
    for letra in palavra_secreta:
        if letra in letras_adivinhadas:
            palavra_atual += letra
        else:
            palavra_atual += '_'
    print(palavra_atual)
    
    # verifica se o jogador venceu o jogo
    if palavra_atual == palavra_secreta:
        print('Parabéns, você venceu!')
        break
    
    # lê uma letra do jogador
    letra = input('Digite uma letra: ').lower().strip()[0]
    
    # verifica se a letra já foi adivinhada antes
    if letra in letras_adivinhadas:
        print('Você já tentou essa letra antes.')
        continue
    
    # adiciona a letra à lista de letras adivinhadas
    letras_adivinhadas.append(letra)
    
    # verifica se a letra esta na palavra secreta
    if letra in palavra_secreta:
        print('Letra correta!')
    else:
        print('Letra incorreta.')
        # diminui as tentativas restantes
        tentativas -= 1
        print(f'Você ainda tem {tentativas} tentativas.')
        
    # verifica se o jogador foi enforcado
    if tentativas == 0:
        print(f'Você foi enforcado! A palavra era {palavra_secreta}.')
        break