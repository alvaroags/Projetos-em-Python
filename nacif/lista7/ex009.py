vetor = []
menor=0
maior=0
soma=0
for c in range(5):
    vetor.append(int(input()))
    soma+=vetor[c]
    if(c==0 or vetor[c]<menor):
        menor = vetor[c]
    if(c==0 or vetor[c]>maior):
        maior = vetor[c]
print(menor)
print(maior)
print(soma/5)
cont=0
for c in range(5):
    if(vetor[c]<(soma/5)):
        cont+=1
print(cont)