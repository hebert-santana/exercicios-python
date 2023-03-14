# Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

while True:
    sexo = str(input("Digite F ou M: ")).strip().upper()[0]
    if sexo in 'MF':
        break

def genero(x):
    if x == "F":
        return print("F - Feminino.")
    else:
        return print("M - Masculino")
    
genero(sexo)