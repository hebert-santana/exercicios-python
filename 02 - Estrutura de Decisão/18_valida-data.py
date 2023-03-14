# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

while True:
    data = input("Digite uma data no formato dd/mm/aaaa: ").strip()
    if data[:2].isnumeric() and data[3:5].isnumeric() and data[6:9]:
        print('Campos numéricos validados.')
        if data[2] == '/' and data[5] == '/':
            print(f'\033[32mData {data} foi validada.\033[0m')
            break
        else:
            print('\033[31mData não validada.\033[0m')
    else:
        print('\033[31mData não validada.\033[0m')