matrix = [[0 for c in range(3)] for i in range(3)]
matrix2 = [[0 for c in range(3)] for i in range(3)]
for c in range(3):
    for i in range(3):
        matrix[c][i] = int(input())
print(matrix)
for c in range(3):
    for i in range(3):
        matrix2[c][i] = matrix[2-i][c]
print(matrix2)