matrix1 = [[0 for c in range(4)] for i in range(4)]
matrix2 = [[0 for c in range(4)] for i in range(4)]
matrix3 = [[0 for c in range(4)] for i in range(4)]
for c in range(4):
    for i in range(4):
        matrix1[c][i] = int(input())
for c in range(4):
    for i in range(4):
        matrix2[c][i] = int(input())
for c in range(4):
    for i in range(4):
        if(matrix1[c][i]>matrix2[c][i]):
            matrix3[c][i] = matrix1[c][i] - matrix2[c][i]
        else:
            matrix3[c][i] = matrix2[c][i] - matrix1[c][i]
print(matrix3)