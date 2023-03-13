# Classe Retangulo: Crie uma classe que modele um retangulo:

# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# Crie um programa que utilize esta classe. 
# Ele deve pedir ao usuário que informe as medidades de um local. 
# Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def mudaAresta(self, base, altura):
        self.base = base
        self.altura = altura

    def PerimetroArea(self):
        perimetro = (self.base + self.altura) * 2
        area = self.base * self.altura
        print(f'O perímetro é: {perimetro}')
        print(f'A área é: {area}.')
        return perimetro, area
        
# entrada do usuário
lado1 = float(input('Informe o tamanho da lateral maior: '))
lado2 = float(input('Informe o tamanho da lateral menor: '))

# cria objeto e imprime perímetro e área
meu_retangulo = Retangulo(lado1, lado2)
meu_retangulo.PerimetroArea()




