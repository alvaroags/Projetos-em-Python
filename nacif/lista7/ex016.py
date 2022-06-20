vetor = []
soma=0
for c in range(5):
    vetor.append(int(input()))
for c in range(5):
    if(c<=2):
        soma+= (vetor[c]-vetor[4-c])**3
print(soma)