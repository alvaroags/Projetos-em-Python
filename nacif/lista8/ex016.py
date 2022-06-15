matrix = [[0 for c in range(4)] for i in range(3)]
for c in range(3):
    for i in range(4):
        matrix[c][i] = float(input())
for c in range(3):
    soma=0
    for i in range(4):
         soma+=matrix[c][i]
    print(soma)
for c in range(3):
    for i in range(4):
        print(matrix[c][i])
soma=0
for c in range(3):
    for i in range(4):
        soma+=matrix[c][i]
print(soma)
