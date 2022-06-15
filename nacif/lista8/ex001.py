matrix = [[0 for c in range(5)] for j in range(5)]
for c in range(5):
    for i in range(5):
        matrix[c][i] = int(input(' '))
for c in range(5):
    print(matrix[c][4])