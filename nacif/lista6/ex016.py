vetor1 = []
vetor2 = []
vetor3 = []
for c in range(5):
    vetor1.append(int(input()))
for c in range(5):
    vetor2.append(int(input()))
for c in range(5):
    vetor3.append(vetor1[c])
    vetor3.append(vetor2[c])
print(vetor3)