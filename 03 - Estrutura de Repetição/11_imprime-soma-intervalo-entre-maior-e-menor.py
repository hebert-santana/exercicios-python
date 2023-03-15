# Altere o programa anterior para mostrar no final a soma dos números.

n1 = int(input("Primeiro Número: "))
n2 = int(input("Segundo Número: "))

menor = n1
maior = n2

if n2 < n1:
    menor = n2
    maior = n1

diferenca = maior - menor
print(f'Números inteiros entre {menor} e {maior}:')

numero_intervalo = menor + 1

soma = 0
while diferenca != 1:
    soma += numero_intervalo
    numero_intervalo += 1
    diferenca -= 1
    
print(f'A soma dos números inteiros entre {maior} e {menor} é: {soma}')

