matrix = [[0 for c in range(5)] for i in range(4)]
soma=0
for c in range(4):
    for i in range(5):
        matrix[c][i] = int(input())
        soma+=matrix[c][i]
print(soma)