# Faça um Programa para um caixa eletrônico. 
# O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
# O valor mínimo é de 10 reais e o máximo de 600 reais. 
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.

# Exemplo 1: Para sacar a quantia de 256 reais, 
# o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, 
# o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

while True:
    print('\033[32m============================== CAIXA ELETRÔNICO ==============================\033[0m')
    valor = input("Qual valor deseja sacar? (mínimo R$10 / máximo 600) ").strip()
    
    if valor.isnumeric():
        valor = int(valor)
        if valor >= 10 and valor <= 600:
            print("Saque Válido!")
            valor_string = str(valor)
            if len(valor_string) == 3:
                centena = valor_string[0]
                dezena = valor_string[1]
                if dezena in '9876':
                    notas_50 = '1'
                    dezena = 
                else:
                unidade = valor_string[2]
                print(centena, dezena, unidade)
                break
            else:
                dezena = valor_string[0]
                unidade = valor_string[1]
                print(dezena, unidade)
                break
                
            
            
            
        else:
            print('Valor Inválido.\nMínimo: R$10\nMáximo: R$600.')
    else:
        print('Valor Inválido.\nDigite apenas números.')
        

            
        
        
                       
        
          
       