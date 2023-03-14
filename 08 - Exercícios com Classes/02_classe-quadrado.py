# Classe Quadrado: Crie uma classe que modele um quadrado:

# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
    def __init__(self, aresta):
        self.aresta = aresta
    
    def mudaAresta(self, aresta):
        self.aresta = aresta

    def arestaArea(self):
        print(f'A aresta do quadrado mede: {self.aresta}')
        area = self.aresta ** 2
        print(f'A área do quadrado é: {area}.')
        
# cria objeto e imprime
meu_quadrado = Quadrado(3)
meu_quadrado.arestaArea()
        


