coluna = int(input())
linha = int(input())
matrix = [[0 for c in range(coluna)] for i in range(linha)]
matrix2 = [[0 for c in range(linha)] for i in range(coluna)]
for c in range(linha):
    for i in range(coluna):
        matrix[c][i] = int(input())
print(matrix)
for c in range(coluna):
    for i in range(linha):
        matrix2[c][i] = matrix[i][c]
print(matrix2)