vetor = [0 for c in range(10)]
trocaVetor = [0 for c in range(10)]
for c in range(10):
    vetor[c] = int(input())
for c in range(10):
    print(vetor[c])
for c in range(10):
    trocaVetor[c] = vetor[9-c]
for c in range(10):
    print(trocaVetor[c])
