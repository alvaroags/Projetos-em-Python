matrix = [[0 for c in range(4)]for i in range(1)]
for c in range(1):
    for i in range(4):
        if(i==2):
            matricula = str(matrix[c][0])
            matrix[c][i] = int(matricula[2:5])
        else:
            matrix[c][i] = int(input())
print(matrix)

