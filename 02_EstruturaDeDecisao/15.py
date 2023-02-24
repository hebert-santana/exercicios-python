# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

print("Informe as medidas das arestas do triângulo.")
lado_a = float(input("Lado 1: "))
lado_b = float(input("Lado 2: "))
lado_c = float(input("Lado 3: "))

soma_ab = lado_a + lado_b
soma_ac = lado_a + lado_c
soma_bc = lado_b + lado_c

somas = [soma_ab, soma_ac, soma_bc]

def validarTriangulo (somas_lados, lado1, lado2, lado3):
    for somas_lados in somas:
        if somas_lados > lado1 or somas_lados > lado2 or somas_lados > lado3:
        # ("Triângulo Validado!")
            if lado1 == lado2 and lado2 == lado3:
                return print("Triângulo Equilátero: três lados iguais!")
            elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
                return print("Triângulo Escaleno: três lados diferentes!")
            else:
                return print("Triângulo Isósceles: quaisquer dois lados iguais!")
        else:
            return print("As medidas não formam um triângulo válido!")
    
validarTriangulo(soma_ab, lado_a, lado_b, lado_c)