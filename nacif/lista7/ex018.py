vetor = [0 for c in range(5)]
vetor2 = [0 for c in range(5)]
for c in range(5):
    num = int(input())
    vetor[c] = num
    vetor2[c] = num
print(vetor2)
for c in range(5):
    for i in range(5):
        if(vetor2[c]<vetor2[i]):
            aux = vetor2[c]
            vetor2[c] = vetor2[i]
            vetor2[i] = aux
for c in range(5):
    for i in range(5):
        if(vetor2[c]==vetor[i]):
            print(f'{vetor2[c]} {i}')