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
        if self.idade < 21:
            self.altura = self.altura + 0.05 * anos
        # idade   
        self.idade = self.idade + anos
        
    def engordar(self, kg):
        self.peso = self.peso + kg
    
    def emagrecer(self, kg):
        self.peso = self.peso - kg
        
    def crescer(self, cm):
        self.altura = self.altura + cm
            
pessoa1 = Pessoa('Hebert', 20, 82.2, 1.81)
print(pessoa1.nome)
print(pessoa1.idade)
print(pessoa1.peso)
print(pessoa1.altura)

pessoa1.envelhecer(2)
print(pessoa1.idade)
print(pessoa1.altura)


            