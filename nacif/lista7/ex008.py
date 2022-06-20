vetor1 = []
vetor2 = []
for c in range(5):
    vetor1.append(int(input()))
for c in range(5):
    vetor2.append(vetor1[4-c])
print(vetor1)
print(vetor2)