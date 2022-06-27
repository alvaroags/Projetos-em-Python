matrix = [[0 for c in range(3)] for i in range(3)]
prodP=1
prodS=1
for c in range(3):
    for i in range(3):
        matrix[c][i] = int(input())
print(matrix)
for c in range(3):
    for i in range(3):
        prodP*=matrix[c][c]
        prodS*=matrix[2-c][c]
print(prodP-prodS)