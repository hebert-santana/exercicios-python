# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 

print("\n******************* Calculadora em Python *******************")

print("Selecione a operação desejada: \n 1 - Somar \n 2 - Subtrair \n 3 - Multiplicar \n 4 - Dividir \n 5 - Potência \n 6 - Módulo")

operacao = int(input("Informe a opção de operação (1/2/3/4/5/6): "))

# validando a operação ou parar programa
import sys

if operacao >= 1 and operacao <= 6:
    print("Operação é Válida!")
else:
    print("Operação Inválida!")
    sys.exit(0)

# informando números
num1 = float(input("Primeiro Número: "))
num2 = float(input("Segundo Número: "))

# função para cálculo e resultado
def operacoes(n1, n2, operador):
    if operador == 1:
        r = n1 + n2
        op = ' + '
        return r, op
    elif operador == 2:
        r = n1 - n2
        op = ' - '
        return r, op
    elif operador == 3:
        r = n1 * n2
        op = ' * '
        return r, op
    elif operador == 4:
        r = n1 / n2
        return r
    elif operador == 5:
        r = n1 ** n2
        op = ' ** '
        return r, op
    elif operador == 6:
        r = n1 % n2
        op = ' % '
        return r, op
    else:
        print("Erro Inesperado!")
        sys.exit(0)

# executando a função e atribuindo retornos à uma lista
lista_resultado = operacoes(num1, num2, operacao)
# print(lista_resultado)
resultado = lista_resultado[0]
operador = lista_resultado[1]

# resposta
print(num1, operador, num2, " = ", resultado)
    

