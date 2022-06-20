vetor = []
for c in range(20):
    vetor.append(int(input()))
    if(c%2==0):
        vetor[c] = 0
for c in range(20):
    print(vetor[c])