# Conta espaços e vogais. 
# Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
#
# quantos espaços em branco existem na frase.
# quantas vezes aparecem as vogais a, e, i, o, u.
print('===================== CONTA ESPAÇOS E VOGAIS =====================')

string = str(input("Frase: ")).lower()

conta_branco = 0
conta_a = 0
conta_e = 0
conta_i = 0
conta_o = 0
conta_u = 0

for i in string:
    if i == ' ':
        conta_branco += 1
    elif i == 'a':
        conta_a += 1
    elif i == 'e':
        conta_e += 1
    elif i == 'i':
        conta_i += 1
    elif i == 'o':
        conta_o += 1
    elif i == 'u':
        conta_u += 1
        
print(f'A frase "{string}" possui {conta_branco} espaços em branco.')
print(f'a: {conta_a} ocorrencias\ne: {conta_e} ocorrencias\ni: {conta_i} ocorrencias\no: {conta_o} ocorrencias\nu: {conta_u} ocorrencias')
print('===================== ====================== =====================')