vetor = []
maior=0
menor=0
for c in range(5):
    vetor.append(int(input()))
    if(vetor[c]>maior or c==0):
        maior = vetor[c]
    if(vetor[c]<menor or c==0):
        menor = vetor[c]
print(maior)
print(menor)