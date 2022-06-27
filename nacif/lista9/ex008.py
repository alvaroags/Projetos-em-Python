vetor1 = []
vetor2 = []
vetor3 = []
vetor4 = []
vetor5 = []
vetor6 = []
matrix = [[0 for c in range(10)]for i in range(10)]
for c in range(10):
    for i in range(10):
        matrix[c][i] = c+i
print(matrix)
for c in range(10):
    vetor1.append(matrix[1][c])
    vetor2.append(matrix[7][c])
    vetor3.append(matrix[c][3])
    vetor4.append(matrix[c][9])
    vetor5.append(matrix[c][c])
    vetor6.append(matrix[c][9-c])
for c in range(10):
    matrix[1][c] = vetor2[c]
    matrix[7][c] = vetor1[c]
    matrix[c][3] = vetor4[c]
    matrix[c][9] = vetor3[c]
    matrix[c][c] = vetor6[c]
    matrix[c][9-c] = vetor5[c]
print(matrix)