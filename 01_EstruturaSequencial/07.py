# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

# inserindo o lado do quadrado
lado_quadrado = float(input("Digite o tamanho do lado do quadrado: "))

# calculando a área e o dobro da área
area = lado_quadrado**2
area_dobro = area * 2

# imprimindo o resultado
print(f"O dobro da área do quadrado é: {area_dobro}")