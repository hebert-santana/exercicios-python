# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    nome = input("Seu nome: ").strip().lower()
    senha = input("Senha: ").strip().lower()

    if nome != senha:
        print('Validado.')
        break       
    else:
     print('O nome de usuário deve ser diferente da senha.')
        