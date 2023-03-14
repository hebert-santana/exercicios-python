# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho = float(input("Qual o tamanho do arquivo (MB)? "))
velocidade = float(input("Qual a velocidade (Mbps)? "))

tempo_seg = tamanho / velocidade
tempo_minutos = round(tempo_seg / 60, 2)

print(f"Tempo aproximado de download: {tempo_minutos} minutos.")