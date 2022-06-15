matrix = [[0 for c in range(4)] for i in range(3)]
matrix2 = [[0 for c in range(4)] for i in range(3)]
for c in range(3):
    for i in range(4):
        matrix[c][i] = int(input())
        matrix2[c][i] = matrix[c][i]*3
print(matrix2)