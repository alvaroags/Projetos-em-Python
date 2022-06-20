vetor = []
vetor2 = []
n = int(input())
for c in range(n):
    vetor.append(int(input()))
for c in range(n):
    cont=0
    for i in range(c,n):
        if(vetor[c]==vetor[i] and i!=c):
            cont+=1
            vetor[i]=0
    if(vetor[c]!=0 and cont>0):
        print(f'{vetor[c]} repete {cont}x')
        vetor[c]=0
for c in range(n):
    if(vetor[c]!=0):
        vetor2.append(vetor[c])
print(vetor2)
    