# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

data = input("Digite uma data no formato dd/mm/aaaa: ")

# decompondo dados em listas
for digito in data:
    dias = [int(data[0]), int(data[1])]
    mes = [int(data[3]), int(data[4])]
    ano = [int(data[6]), int(data[7]), int(data[8]), int(data[9])]
    barra = [data[2], data[5]]
    
# condição para as datas e o separador "/"
if dias[0] > 3:
    print("Data não válida! O campo dias apresenta erro.")
elif mes[0] > 1:
    print("Data não válida! O campo mês apresenta erro.")
elif ano[0] > 2:
    print("Data não válida! O campo ano apresenta erro.")
elif barra[0] != "/" or barra[1] != "/":
    print("Data não válida! Use '/' para separar dd/mm/aaaa")
else:
    print("Data foi validada!")