matrix = [[0 for c in range(5)] for c in range(2)]
maior = [0 for c in range(2)]
for c in range(2):
    for i in range(5):
        matrix[c][i] = int(input())
for c in range(2):
    for i in range(5):
        if(matrix[c][i]>maior[c]):
            maior[c] = matrix[c][i]
for c in range(2):
    print(maior[c])