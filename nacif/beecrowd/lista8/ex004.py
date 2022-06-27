matrix = [[0 for c in range(12)] for i in range(12)]
op = str(input())
for c in range(12):
    for i in range(12):
        matrix[c][i] = float(input())
soma=0
for c in range(12):
    for i in range(12):
        if(c>i and c>(11-i)):
            soma+=matrix[c][i]
if(op=='S'):
    print(f'{soma:.1f}')
elif(op=='M'):
    print(f'{soma/30:.1f}')