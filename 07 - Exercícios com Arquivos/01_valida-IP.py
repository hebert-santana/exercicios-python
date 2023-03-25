# Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.

# Um endereço IP válido deve conter exatamente 4 partes, separadas por pontos.
# Cada parte deve ser um número inteiro entre 0 e 255.

# verifica se um endereço IP é válido (True / False)
def verificaIP(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or int(part) > 255:
            return False
    return True


# lê o arquivo de entrada
with open('enderecos.txt', 'r') as f:
    ips = [line.strip() for line in f]

# separa os IPs validos e invalidos
valid_ips = []
invalid_ips = []
for ip in ips:
    if verificaIP(ip):
        valid_ips.append(ip)
    else:
        invalid_ips.append(ip)

# escreve o relatorio no arquivo de saida
with open('relatorio.txt', 'w') as f:
    f.write('[Enderecos validos:]\n')
    for ip in valid_ips:
        f.write(ip + '\n')
    f.write('\n[Enderecos invalidos:]\n')
    for ip in invalid_ips:
        f.write(ip + '\n')
