# Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir(). 
# Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. 
# Experimente fazer com que um macaco coma o outro. 
# É possível criar um macaco canibal?

class Macaco:
    def __init__(self, nome, bucho, peso=10):
        self.nome = nome
        self.bucho = min(max(bucho, 0), 5)
        self.peso = min(max(peso, 2), 50)
        
    def comer(self, kg):
        if (self.bucho + kg) <= 5 and (self.peso + kg) <= 50:
            self.bucho += kg
            self.peso += kg
        else:
            print('Não pode fazer essa refeição. Faça a digestão da refeição anterior primeiro.')
            
    def verBucho(self):
        print(f'Peso no Bucho: {self.bucho}.')
        
    def digerir(self):
        self.bucho = 0
        
        
macaco1 = Macaco('Able', 0, 15)
macaco2 = Macaco('Baker', 2, 25)
print(f'{macaco1.nome}\nBucho: {macaco1.bucho}\nPeso: {macaco1.peso}')
print(f'{macaco2.nome}\nBucho: {macaco2.bucho}\nPeso: {macaco2.peso}')

macaco1.comer(2)
print(f'{macaco1.nome}\nBucho: {macaco1.bucho}\nPeso: {macaco1.peso}')
macaco1.comer(1)
print(f'{macaco1.nome}\nBucho: {macaco1.bucho}\nPeso: {macaco1.peso}')
macaco1.comer(0.5)
print(f'{macaco1.nome}\nBucho: {macaco1.bucho}\nPeso: {macaco1.peso}')

macaco2.comer(1)
print(f'{macaco2.nome}\nBucho: {macaco2.bucho}\nPeso: {macaco2.peso}')
macaco2.comer(1)
print(f'{macaco2.nome}\nBucho: {macaco2.bucho}\nPeso: {macaco2.peso}')
macaco2.comer(5.25)
print(f'{macaco2.nome}\nBucho: {macaco2.bucho}\nPeso: {macaco2.peso}')
        