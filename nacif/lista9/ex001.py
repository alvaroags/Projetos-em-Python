matrix = [[0 for c in range(10)] for i in range(10)]
for c in range(3):
    for i in range(3):
        matrix[c][i] = int(input())
for c in range(3):
    for i in range(3):
        if(c!=i):
            print(f'{matrix[c][i]}', end=' ')
