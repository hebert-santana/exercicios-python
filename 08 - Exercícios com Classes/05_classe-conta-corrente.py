# Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 
# A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.

class ContaCorrente:
    def __init__(self, numero, nome, saldo=0):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo
    
    def alterarNome(self, novo_nome):
        self.nome = novo_nome
    
    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito Realizado.\nNovo saldo: R$ {self.saldo}')
    
    def sacar(self, valor):
        if (self.saldo - valor) > 0:
            self.saldo -= valor
            print(f'Saque Realizado.\nNovo saldo: R$ {self.saldo}')
        else:
            print('Saldo Insuficiente.')
            

conta1 = ContaCorrente('001', 'Hebert', 100)
conta2 = ContaCorrente('002', 'Maya')

print(f'\n===== Conta Corrente 01 =====\nNúmero: {conta1.numero}\nNome: {conta1.nome}\nSaldo: {conta1.saldo}')
print(f'\n\033[33m===== Conta Corrente 02 =====\nNome: {conta2.numero}\nNome: {conta2.nome}\nSaldo: {conta2.saldo}')

print(f'\n\033[32m===== DEPÓSITO R$50,00 =====\033[0m')
conta1.depositar(50)
conta2.depositar(50)

print(f'\n===== Conta Corrente 01 =====\nNúmero: {conta1.numero}\nNome: {conta1.nome}\nSaldo: {conta1.saldo}')
print(f'\n\033[33m===== Conta Corrente 02 =====\nNome: {conta2.numero}\nNome: {conta2.nome}\nSaldo: {conta2.saldo}')

print(f'\n\033[32m===== SACANDO R$100,00 =====\033[0m')
conta1.sacar(100)
conta2.sacar(100)

print(f'\n===== Conta Corrente 01 =====\nNúmero: {conta1.numero}\nNome: {conta1.nome}\nSaldo: {conta1.saldo}')
print(f'\n\033[33m===== Conta Corrente 02 =====\nNome: {conta2.numero}\nNome: {conta2.nome}\nSaldo: {conta2.saldo}')
        