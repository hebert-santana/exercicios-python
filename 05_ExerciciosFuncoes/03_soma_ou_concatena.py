# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def soma(a, b, c):    
    somas = a + b + c
    return somas

# se todos argumentos são do tipo numérico ou uma string de números; converte
def converte(a, b, c):
    if isinstance(a, str) and a.isnumeric():
        if isinstance(b, str) and b.isnumeric():
             if isinstance(c, str) and c.isnumeric():
                 a = float(a)    
                 b = float(b)
                 c = float(c)
                      
    return a, b, c

    
n1 = input('Argumento 1: ')
n2 = input('Argumento 2: ')
n3 = input('Argumento 3: ')


arg1, arg2, arg3 = converte(n1, n2, n3)

print(soma(arg1, arg2, arg3))