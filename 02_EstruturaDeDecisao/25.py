# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" 
# 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

telefone = input("Telefonou para a vítima? (s/n) ")
no_local = input("Esteve no local do crime? (s/n) ")
mora_perto = input("Mora perto da vítima? (s/n) " )
divida = input("Devia para a vítima? (s/n) ")
trabalho = input("Já trabalhou com a vítima? (s/n) " )

# contando pontuação de suspeita
contador = 0
if telefone == "s":
    contador = contador + 1
    
if no_local == "s":
    contador = contador + 1
        
if mora_perto == "s":
    contador = contador + 1
            
if divida == "s":
    contador = contador + 1
                
if trabalho == "s":
    contador = contador + 1
    
# função para classificar pontuação
def classificaSuspeito(p):
    if p == 5:
        pessoa = "Assassino"
    elif p == 4 or p == 3:
        pessoa = "Cúmplice"
    elif p == 2:
        pessoa = "Suspeita"
    else:
        pessoa = "Inocente"
    return pessoa

# resultado
resultado = classificaSuspeito(contador)
print(resultado)



