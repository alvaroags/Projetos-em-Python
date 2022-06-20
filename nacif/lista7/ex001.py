vetor = []
soma=0
for c in range(10):
    vetor.append(int(input()))
    soma+=vetor[c]
for c in range(10):
    print(vetor[c])
print(soma/10)