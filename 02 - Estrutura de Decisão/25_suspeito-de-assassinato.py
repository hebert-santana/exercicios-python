# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" 
# 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

nome = input('Nome do suspeito: ')
tel = input("Telefonou para a vítima? (s/n) ").strip().lower()
no_local = input("Esteve no local do crime? (s/n) ").strip().lower()
mora_perto = input("Mora perto da vítima? (s/n) " ).strip().lower()
divida = input("Devia para a vítima? (s/n) ").strip().lower()
trabalho = input("Já trabalhou com a vítima? (s/n) " ).strip().lower()

# contando pontuação de suspeita
contador = 0
if tel == 's':
    contador += 1    
if no_local == 's':
    contador += 1        
if mora_perto == 's':
    contador += 1            
if divida == 's':
    contador += 1                
if trabalho == 's':
    contador += 1
    

if contador == 5:
    pessoa = "Assassino"
elif contador == 4 or contador == 3:
    pessoa = "Cúmplice"
elif contador == 2:
    pessoa = "Suspeita"
else:
    pessoa = "Inocente"


print(f'{nome} é um {pessoa}')



