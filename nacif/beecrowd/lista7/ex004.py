vetor = [[0 for c in range(4)] for c in range(4)]
soma=0
cont=0
O = str(input())
for c in range(4):
    for i in range(4):
        vetor[c][i] = float(input())
for c in range(4):
    for c in range(4):
        if((c+i)>11 and (i-c)>0):
            soma+=vetor[c][i]
            cont+=1
if(O=='S'):
    print(f'{soma:.1f}')
else:
    print(f'{soma/cont:.1f}')
            