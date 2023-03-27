# Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). 
# Após esta entrada de dados, faça:
# a) Mostre a quantidade de valores que foram lidos;
# b) Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# c) Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# d) Calcule e mostre a soma dos valores;
# e) Calcule e mostre a média dos valores;
# f) Calcule e mostre a quantidade de valores acima da média calculada;
# g) Calcule e mostre a quantidade de valores abaixo de sete;
# h) Encerre o programa com uma mensagem;

notas = []

while True:
    nota = float(input('Digite uma nota ou -1 para encerrar: '))
    if nota != -1:
        notas.append(nota)
    else:
        break

print('\n\n===================================== INÍCIO =====================================')
# a)

print('Quantidade de notas lidas: ', len(notas))

# b)
print('Valores informados: ', end='')
for nota in notas:
    print(nota, end=' ')
print()

# c)
print('============================ Valores na ordem inversa ============================')
for nota in reversed(notas):
    print(nota)
print('============================ ======================== ============================')

# d)
soma = sum(notas)
print(f'Soma dos valores: {soma}')

# e)
media = soma / len(notas)
print(f'Média dos valores: {media}')

# f/g)
acima_media = 0
abaixo_sete = 0
for nota in notas:
    if nota > media:
        acima_media += 1
    if nota < 7:
        abaixo_sete += 1

print(f'Quantidade de valores acima da média: {acima_media}')
print(f'Quantidade de valores abaixo de sete: {abaixo_sete}')

# h)
print('Encerrando programa...\nPrograma encerrado.')
print('\n============================ ======================== ============================')
