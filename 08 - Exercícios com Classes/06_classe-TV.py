# Classe TV: Faça um programa que simule um televisor criando-o como um objeto. 
# O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. 
# Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.


class Televisao:
    def __init__(self, canal=1, volume=0):
        self.canal = min(max(canal, 1), 20)
        self.volume = min(max(volume, 0), 50)
    
    def alteraVolume(self, novo_volume):
        if novo_volume <= 50 and novo_volume >= 0: 
            self.volume = novo_volume

    def alteraCanal(self, novo_canal):
        if novo_canal >= 1 and novo_canal <= 20:
            self.canal = novo_canal
            
            
televisao_01 = Televisao(8, 10)
print(f'TV 01 no canal {televisao_01.canal} com o volume {televisao_01.volume}')
televisao_01.alteraVolume(22)
televisao_01.alteraCanal(13)
print(f'TV 01 no canal {televisao_01.canal} com o volume {televisao_01.volume}')


televisao_02 = Televisao(55, 100)
print(f'TV 02 no canal {televisao_02.canal} com o volume {televisao_02.volume}')

televisao_03 = Televisao()
print(f'TV 03 no canal {televisao_03.canal} com o volume {televisao_03.volume}')
