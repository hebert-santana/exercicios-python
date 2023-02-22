# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado_quadrado = float(input("Digite o tamanho do lado do quadrado: "))

area = lado_quadrado**2
area_dobro = area * 2

print("O dobro da área do quadrado é: ", area_dobro)