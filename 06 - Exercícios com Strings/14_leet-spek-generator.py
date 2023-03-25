# Leet spek generator. 
# Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras, como números por exemplo. 
# A própria palavra leet admite muitas variações, como l33t ou 1337. O uso do leet reflete uma subcultura relacionada ao mundo dos jogos de computador e internet, sendo muito usada para confundir os iniciantes e afirmar-se como parte de um grupo. 
# Pesquise sobre as principais formas de traduzir as letras. 
# Depois, faça um programa que peça uma texto e transforme-o para a grafia leet speak.

dicionario_leet = {
    "a": "4",
    "b": "8",
    "e": "3",
    "g": "9",
    "i": "!",
    "l": "1",
    "o": "0",
    "s": "5",
    "t": "7",
    "z": "2"
}

def leet_speak(texto):
    resultado = ""
    for letra in texto:
        if letra in dicionario_leet:
            resultado += dicionario_leet[letra]
        else:
            resultado += letra
    return resultado

texto = input("Digite um texto para ser transformado em leet speak: ").lower().strip()
texto_leet = leet_speak(texto)
print(f'Texto em leet speak:\n{texto_leet}')
