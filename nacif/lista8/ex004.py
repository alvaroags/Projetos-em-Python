matrix = [[0 for c in range(3)] for i in range(3)]
for c in range(3):
    for i in range(3):
        matrix[c][i] = int(input())
for c in range(3):
    print(matrix[c][c])