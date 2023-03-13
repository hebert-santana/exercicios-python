# Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

# Atributos: Nome, Fome, Saúde e Idade 
# b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade 
# Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, 
# ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.


class Tamagushi:
    def __init__(self, nome, fome=0, saude=10, idade=0):
        self.nome = nome
        self.fome = min(max(fome, 0), 5)
        self.saude = min(max(saude, 0), 10)
        self.idade = min(max(idade, 0), 99)
        self.humor = self.saude - self.fome
        

maya = Tamagushi('maya', 100, 10, 4)

print(f'Nome: {maya.nome}')
print(f'Fome: {maya.fome}')
print(f'Saúde: {maya.saude}')
print(f'Idade: {maya.idade}')
print(f'Humor: {maya.humor}')
        
        
    