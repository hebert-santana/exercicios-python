# Classe Bola: Crie uma classe que modele uma bola:

# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    
    def trocaCor(self, cor):
        self.cor = cor

    def mostraCor(self):
        print(f'A nova cor é: {self.cor}.')
        
# cria o objeto        
minha_bola = Bola('Verde', 20, 'Plástico')

# imprimindo o objeto
print(minha_bola.cor)
print(minha_bola.circunferencia)
print(minha_bola.material)

# muda a cor e imprime
minha_bola.trocaCor('Azul')
minha_bola.mostraCor()