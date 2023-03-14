# Faça um Programa que pergunte em que turno você estuda. 
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
while True:
    print("Digite: \n [M] para Matutino \n [V] para Vespertino \n [N] para Noturno")
    turno = str(input("Em qual turno você estuda? ")).strip().upper()[0]
    if turno in 'MVN':
        break

def saudacao(x):
    if x == "M":
        return print("Bom dia!")
    elif x == "V":
        return print("Boa tarde!")
    elif x == "N":
        return print("Boa noite!")
    
saudacao(turno)