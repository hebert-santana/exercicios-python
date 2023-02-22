# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print("Digite: \n M para Matutino \n V para Vespertino \n N para Noturno")
turno = input("Em qual turno você estuda? ")

# passar para maiúsculo caso usuário digite em minúsculo
turno = turno.upper()

def saudacao(x):
    if x == "M":
        return print("Bom dia!")
    elif x == "V":
        return print("Boa tarde!")
    elif x == "N":
        return print("Boa noite!")
    else:
        return print("Valor Inválido!")
    
saudacao(turno)