n = int(input())
matrix = [[0 for c in range(n)] for i in range(n)]
matrixT = [[0 for c in range(n)] for i in range(n)]
for c in range(n):
    for i in range(n):
        matrix[c][i] = int(input())
        matrixT[i][c] = matrix[c][i]
if(matrix[c][i]!=matrixT[c][i]):
    print('Simetrica')
else:
    print('Assimetrica')