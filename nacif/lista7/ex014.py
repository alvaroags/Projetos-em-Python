vetor = []
n = int(input())
for c in range(n):
    vetor.append(int(input()))
for c in range(n):
    for i in range(n):
        if(vetor[c]<vetor[i]):
            aux = vetor[c]
            vetor[c] = vetor[i]
            vetor[i] = aux
print(vetor)
for c in range(n):
    for i in range(n):
        if(vetor[c]>vetor[i]):
            aux = vetor[c]
            vetor[c] = vetor[i]
            vetor[i] = aux
print(vetor)