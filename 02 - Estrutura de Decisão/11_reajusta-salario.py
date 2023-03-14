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
print(f"\033[33m========================== CALCULO REAJUSTE ==========================\033[0m")

salario_funcionario = int(input("Digite o salário: R$ "))

# Função para comprar o valor e aplicar o reajuste
def reajuste(salario):
    if salario >= 1500:
        fator = 1.05
        reajustado = salario * fator
        aumento = reajustado - salario
    elif salario >= 700:
        fator = 1.1
        reajustado = salario * fator
        aumento = reajustado - salario
    elif salario > 280:
        fator = 1.15
        reajustado = salario * fator
        aumento = reajustado - salario
    elif salario <= 280 and salario > 0:
        fator = 1.2
        reajustado = salario * fator
        aumento = reajustado - salario
    else:
        return print("Valor Inválido!")
    return fator, reajustado, aumento
    
fator_correcao, salario_reajustado, aumento_total = reajuste(salario_funcionario)
fator_correcao = (fator_correcao - 1) * 100

print(f'Seu salário era R$ {round(salario_funcionario)} e foi reajustado em {round(fator_correcao)}% (R$ {round(aumento_total)}).\nSalário Reajustado: R$ {round(salario_reajustado)}')

print(f"\033[33m========================== ================ ==========================\033[0m")

    

    

    