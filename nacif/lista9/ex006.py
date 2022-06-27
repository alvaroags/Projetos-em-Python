matrix = [[0 for c in range(3)] for i in range(3)]
for c in range(3):
    matrix[c][0] = str(input())
    ideal = int(input())
    estoque = int(input())
    matrix[c][1] = ideal - estoque
for c in range(3):
    if(matrix[c][1]>0):
        print(f'{matrix[c][0]} {matrix[c][1]}')