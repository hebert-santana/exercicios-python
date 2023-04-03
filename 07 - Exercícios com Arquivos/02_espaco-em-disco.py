def converte_para_mb(tamanho_bytes):
    """
    a função converte o tamanho em bytes para megabytes
    """
    tamanho_mb = tamanho_bytes / (1024 * 1024)
    return tamanho_mb


def calcula_percentual_uso(tamanho_bytes, tamanho_total):
    """
    a função calcula o percentual de uso de um determinado espaço em relação ao espaço total
    """
    percentual = (tamanho_bytes / tamanho_total) * 100
    return percentual


# leitura do arquivo de usuários
with open('usuarios.txt', 'r') as arquivo:
    usuarios = arquivo.readlines()

# cálculo do espaço total ocupado pelos usuários
tamanho_total = sum(int(usuario.split()[1]) for usuario in usuarios)

# criação do relatório
with open('relatorio.txt', 'w') as arquivo:
    arquivo.write('ACME Inc.               Uso do espaco em disco pelos usuarios\n')
    arquivo.write('------------------------------------------------------------------------\n')
    arquivo.write('Nr.  Usuario        Espaco utilizado     % do uso\n\n')
    
    for i, usuario in enumerate(usuarios, start=1):
        nome, tamanho_bytes = usuario.split()
        tamanho_mb = converte_para_mb(int(tamanho_bytes))
        percentual_uso = calcula_percentual_uso(int(tamanho_bytes), tamanho_total)
        
        arquivo.write(f'{i:<5}{nome:<15}{tamanho_mb:>15.2f} MB{percentual_uso:>15.2f}%\n')
        
    # cálculo e escrita do espaço total ocupado e médio ocupado
    espaco_total_mb = converte_para_mb(tamanho_total)
    espaco_medio_mb = espaco_total_mb / len(usuarios)
    
    arquivo.write(f'\nEspaco total ocupado: {espaco_total_mb:.2f} MB\n')
    arquivo.write(f'Espaco medio ocupado: {espaco_medio_mb:.2f} MB\n')
