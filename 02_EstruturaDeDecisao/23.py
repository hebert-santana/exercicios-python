# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 
# Dica: utilize uma função de arredondamento.

num = input("Digite um número: ")

# considera por padrão que seja inteiro
numero = "inteiro"

# loop na str, se encontrar "." o número é decimal
for digitos in num:
    if "." in digitos:
        numero = "decimal"
        
print(numero)

        