tamanhoVetor = int(input())
vetor = []
for c in range(tamanhoVetor):
    vetor.append(int(input()))
for c in range(tamanhoVetor):
    if(c%2==0):
        print(vetor[c])