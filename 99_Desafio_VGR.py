def somar_matrizes(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        return print('Matrizes devem conter o mesmo numero de linhas e colunas')
    result = []
    for i in range(len(matriz1[:1])):
        result.append([])
        for j in range(len(matriz2[:4])):
            result[i].append(matriz1[i][j] * matriz2[j][i])
    soma = sum(result.pop())
    return print(f"Resultado da soma linha x coluna: {soma}")


somar_matrizes(
    matriz1=[[35, 42, 1, 79],
             [44, 29, 77, 71],
             [25, 64, 15, 34],
             [98, 73, 15, 85]],
    matriz2=[[44, 86, 68, 46],
             [11, 61, 97, 52],
             [62, 38, 30, 66],
             [93, 57, 38, 39]])

# 35*44 + 42*11 + 1*62 + 79*46
# 1540 + 462 + 62 + 7347 = 9411