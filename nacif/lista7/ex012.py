vetor = []
for c in range(6):
    vetor.append(int(input()))
for c in range(6):
    cont=1
    for i in range(c,6):
        if(vetor[c]==vetor[i] and c!=i):
            cont+=1
            vetor[i] = 0
    if(vetor[c]!=0):
        freqAbs = cont
        freqRel = (cont/6)*100
        print(f'{vetor[c]} {freqAbs} {freqRel:.2f}%')
    
