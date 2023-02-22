# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input("Digite F ou M: ")

def genero(x):
    if x == "F":
        return print("F - Feminino.")
    elif x == "M":
        return print("M - Masculino")
    else:
        return print("Sexo Inválido")
    
genero(sexo)