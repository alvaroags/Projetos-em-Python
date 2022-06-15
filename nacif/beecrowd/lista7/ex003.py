vetor = [[0 for c in range(12)] for c in range(12)]
soma=0
cont=0
O = str(input())
for c in range(12):
    for i in range(12):
        vetor[c][i]=float(input())
for c in range(12):
    for i in range(12):
        if((c+i)>11):
            soma+=vetor[c][i]
            cont+=1
if(O=='S'):
    print(f'{soma/cont:.2f}')
else:
    print(f'{soma/cont:.2f}')