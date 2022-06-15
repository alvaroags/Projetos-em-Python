vetor = [[0 for c in range(12)] for i in range(12)]
soma=0
L = int(input())
T = str(input())
for c in range(12):
    for i in range(12):
        vetor[c][i] = float(input())
for c in range(12):
    soma+=vetor[L][c]
if(T=='S' or T=='s'):
    print(f'{soma:.1f}')
elif(T=='M' or T=='m'):
    print(f'{(soma/12):.1f}')