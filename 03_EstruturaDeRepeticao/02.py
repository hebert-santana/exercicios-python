# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nome = input("Seu nome: ")
senha = input("Senha: ")

if nome == senha:
    while nome == senha:
        print("Erro!")
        nome = input("Seu nome: ")
        senha = input("Senha: ")


print("Nome e senha validada.")
        