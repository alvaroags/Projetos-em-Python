achou=0
matrix = [[0 for c in range(3)] for i in range(3)]
for c in range(3):
    for i in range(3):
        matrix[c][i] = int(input(' '))
N = int(input('VALOR DE N: '))
for c in range(3):
    for i in range(3):
        if(matrix[c][i]==N):
            print(matrix[c][i])
            achou = 1
        elif(matrix[2][2]!=N and c==2 and i==2 and achou!=1):
            print('Numero nao encontrado')