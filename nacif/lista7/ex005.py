vetor = []
for c in range(5):
    vetor.append(int(input()))
for c in range(5):
    cont=0
    for i in range(1,vetor[c]):
        if(vetor[c]%i==0):
            cont+=1
    if(cont<=2):
        print(f'{vetor[c]}', end=' ')
        print(c)