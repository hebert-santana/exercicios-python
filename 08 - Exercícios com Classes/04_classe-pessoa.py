# Classe Pessoa: Crie uma classe que modele uma pessoa:

# Atributos: nome, idade, peso e altura
# Métodos: Envelhercer, engordar, emagrecer, crescer. 
# Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 5 cm.

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def envelhecer(self, anos):
        # crescimento
        ano = 0            
        while (21 - self.idade) > 0:
            self.altura += 0.05
            ano += 1
            self.idade += 1
            if ano == anos:
                break
        
    def engordar(self, kg):
        self.peso += kg
    
    def emagrecer(self, kg):
        if (self.peso - kg) > 0:
            self.peso -= kg
        
    def crescer(self, cm):
        self.altura += cm
            
pessoa1 = Pessoa('Hebert', 20, 82.2, 1.81)
pessoa2 = Pessoa('Maya', 4, 35, 1.42)
print(f'\n===== PESSOA 01 =====\nNome: {pessoa1.nome}\nIdade: {pessoa1.idade}\nPeso: {pessoa1.peso}\nAltura: {pessoa1.altura}')
print(f'\n\033[33m===== PESSOA 02 =====\nNome: {pessoa2.nome}\nIdade: {pessoa2.idade}\nPeso: {pessoa2.peso}\nAltura: {pessoa2.altura}\033[0m')

print(f'\n\033[32m===== ENVELHECER 2 anos =====\033[0m')
pessoa1.envelhecer(2)
pessoa2.envelhecer(2)

print(f'\n===== PESSOA 01 =====\nNome: {pessoa1.nome}\nIdade: {pessoa1.idade}\nPeso: {pessoa1.peso}\nAltura: {pessoa1.altura}')
print(f'\n\033[33m===== PESSOA 02 =====\nNome: {pessoa2.nome}\nIdade: {pessoa2.idade}\nPeso: {pessoa2.peso}\nAltura: {pessoa2.altura}\033[0m')



            