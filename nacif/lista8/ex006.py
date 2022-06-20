matrix = [[0 for c in range(3)] for i in range(3)]
soma=0
for c in range(3):
    for i in range(3):
        matrix[c][i] = int(input())
for c in range(3):
    for i in range(3):
        if(i>c):
            print(matrix[c][i])
print(matrix)