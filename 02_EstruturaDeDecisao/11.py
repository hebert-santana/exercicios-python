# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# a. salários até R$ 280,00 (incluindo) : aumento de 20%
# b. salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# c. salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# d. salários de R$ 1500,00 em diante : aumento de 5% 
# 
# Após os aumentos serem realizados, informe na tela:
# e. o salário antes do reajuste;
# f. o percentual de aumento aplicado;
# g. o valor do aumento;
# h. o novo salário, após o aumento.


salario_funcionario = float(input("Digite o salário: "))

# Função para comprar o valor e aplicar o reajuste
def reajuste(salario):
    if salario >= 1500:
        reajustado = salario * 1.05
        aumento = reajustado - salario
        return print("Seu salário era R$", salario, "e foi reajustado em 5% ( R$", aumento, " ). Agora seu salário é R$", reajustado)
    elif salario >= 700:
        reajustado = salario * 1.1
        aumento = reajustado - salario
        return print("Seu salário era R$", salario, "e foi reajustado em 10% ( R$", aumento, " ). Agora seu salário é R$", reajustado)
    elif salario > 280:
        reajustado = salario * 1.15
        aumento = reajustado - salario
        return print("Seu salário era R$", salario, "e foi reajustado em 15% ( R$", aumento, " ). Agora seu salário é R$", reajustado)
    elif salario <= 280 and salario > 0:
        reajustado = salario * 1.2
        aumento = reajustado - salario
        return print("Seu salário era R$", salario, "e foi reajustado em 20% ( R$", aumento, " ). Agora seu salário é R$", reajustado)
    else:
        return print("Valor Inválido!")
    
reajuste(salario_funcionario)
    

    

    