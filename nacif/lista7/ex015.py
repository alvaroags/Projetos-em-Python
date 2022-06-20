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
    cont=1
    for i in range(n):
        if(vetor[c]==vetor[i] and c!=i):
            cont+=1
            vetor[i] = 0
    if(vetor[c]!=0 and cont>1):
        print(f'{vetor[c]} repete {cont}x')