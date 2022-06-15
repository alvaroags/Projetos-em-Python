matrix = [[0 for c in range(15)] for i in range(15)]
vetor = []
esp = ' '
c = 0
cont=0
while True:
    num = int(input())
    if(num>0):
        vetor.append(num)
        cont+=1
    else:
        break
for x in range(cont):
    for c in range(vetor[x]):
        for i in range(vetor[x]):
            matrix[c][i] = str(2**(c+i))
    tamanho = len(str(matrix[c][i]))
    for c in range(vetor[x]):
        for i in range(vetor[x]):
            espTemp = len(str(matrix[c][i]))
            espTemp = tamanho - espTemp
            if(i==vetor[x-1]):
                print(f'{matrix[c][i]}{(esp) * espTemp}', end=' ')
            else:
                print(f'{matrix[c][i]}{(esp) * espTemp}', end='')
        print()
    