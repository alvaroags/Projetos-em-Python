n = int(input())
matrix = [[0 for c in range(n)] for i in range(n)]
matrixT = [[0 for c in range(n)] for i in range(n)]
matrixO = [[0 for c in range(n)] for i in range(n)]
for c in range(n):
    for i in range(n):
        matrix[c][i] = int(input())
        matrixT[i][c] = matrix[c][i]
        matrixO[c][i] = matrix[c][i]*-1
if(matrixT!=matrixO):
    print('É Anti-Simetrica')
else:
    print('Não é Anti-Simetrica')