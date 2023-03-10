# Tamanho de strings. 
# Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. 
# Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

# Compara duas strings
# String 1: Brasil Hexa 2006
# String 2: Brasil! Hexa 2006!
# Tamanho de "Brasil Hexa 2006": 16 caracteres
# Tamanho de "Brasil! Hexa 2006!": 18 caracteres
# As duas strings são de tamanhos diferentes.
# As duas strings possuem conteúdo diferente.

str1 = input("String 01: ")
str2 = input("String 02: ")

if str1 == str2:
    print("As strings são iguais.")
else:
    print("As strings são diferentes.")
    

print(f'Comprimento de {str1}: {len(str1)} caracteres.')
print(f'Comprimento da {str2}: {len(str2)} caracteres.')
