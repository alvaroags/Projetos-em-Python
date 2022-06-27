matrix = [[0 for c in range(2)] for i in range(2)]
for c in range(2):
    for i in range(2):
        matrix[c][i] = float(input())
print(matrix)
determinante = (matrix[0][0]*matrix[1][1])-(matrix[1][0]*matrix[0][1])
for c in range(2):
    for i in range(2):
        matrix[c][i] = matrix[c][i]/determinante
aux = matrix[0][0]
matrix[0][0] = matrix[1][1]
matrix[1][1] = aux
for c in range(2):
    matrix[1-c][c]*=-1
print(matrix)