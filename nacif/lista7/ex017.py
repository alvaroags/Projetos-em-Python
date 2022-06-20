vetor = []
qt = []
soma=0
for c in range(5):
    vetor.append(float(input()))
    qt.append(int(input()))
for c in range(5):
    soma+=vetor[c]*qt[c]
print(soma)