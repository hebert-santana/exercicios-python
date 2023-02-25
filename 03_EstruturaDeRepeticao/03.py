# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = input("Digite seu nome: ")

while len(nome) <= 3:
    print("Nome Inválido!")
    nome = input("Digite seu nome: ")
    
    
idade = float(input("Digite sua idade: "))
while idade < 0 or idade > 150:
    print("Idade Inválida!")
    idade = float(input("Digite sua idade: "))


salario = float(input("Digite seu salário: "))
while salario < 0:
    print("Salário Inválido!")
    salario = float(input("Digite seu salário: "))
    
    
sexo = input("Digite seu sexo: \n f - feminino \n m - masculino \n")
while sexo != "f" and sexo != "m":
    print("Sexo Inválido!")
    sexo = input("Digite seu sexo: \n f - feminino \n m - masculino \n")


estado_civil = input("Digite seu estado civil: \n s - solteiro \n c - casado \n v - viúvo \n d - divorciado \n")
while estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d":
    print("Estado Civil Inválido!")
    estado_civil = input("Digite seu estado civil: \n s - solteiro \n c - casado \n v - viúvo \n d - divorciado \n")
    
print(nome, "\n idade:", idade, "\n salário: R$", salario, "\n sexo:", sexo, "\n estado civil:", estado_civil)
    
