matrix = [[0 for c in range(5)] for i in range(3)]
vetor = [0 for c in range(3)]
for c in range(3):
    for i in range(5):
        matrix[c][i] = int(input())
for c in range(3):
    for i in range(5):
        vetor[c]+=matrix[c][i]
for c in range(3):
    print(vetor[c])