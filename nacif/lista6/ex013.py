vetor = []
for c in range(15):
    vetor.append(int(input()))
for c in range(15):
    for i in range(15):
        if(vetor[i]<vetor[c]):
            aux = vetor[c]
            vetor[c] = vetor[i]
            vetor[i] = aux
for c in range(15):
    print(vetor[14-c])