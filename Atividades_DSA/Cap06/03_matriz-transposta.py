# Exercício 3 - Calcule a matriz transposta da matriz abaixo.
# Caso não saiba o que é matriz transposta, visite este link: https://pt.wikipedia.org/wiki/Matriz_transposta
# Matriz transposta é um conceito fundamental na construção de redes neurais artificiais, base de sistemas de IA.


matriz = [[1, 2],[3,4],[5,6],[7,8]] 
# matriz é 4 x 2 e vou transformar em 2 x 4

import numpy as np

matriz_transposta = np.transpose(matriz)

print("Matriz Transposta:")
print(matriz_transposta)

