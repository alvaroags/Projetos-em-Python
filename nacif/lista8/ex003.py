matrix = [[0 for c in range(5)] for i in range(7)]
for c in range(7):
    for i in range(5):
        matrix[c][i] = int(input())
        if(matrix[c][i]%2!=0):
            matrix[c][i]*=2
print(matrix)