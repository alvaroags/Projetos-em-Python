vetor = [0 for c in range(5)]
maior=0
menor=0
somaPar=0
somaImpar=0
contPar=0
contImpar=0
for c in range(5):
    vetor.append(int(input()))
    if(vetor[c]%2==0):
        somaPar+=vetor[c]
        contPar+=1
        if(contPar==1 or vetor[c]>maior):
            maior = vetor[c]
    else:
        somaImpar+=vetor[c]
        contImpar+=1
        if(contImpar==1 or vetor[c]<menor):
            menor = vetor[c]
mediaPar = somaPar/contPar
mediaImpar = somaImpar/contImpar
print(f'{maior} maior par')
print(f'{menor} menor impar')
print(f'{mediaPar} media par')
print(f'{mediaImpar} media impar')
for c in range(5):
    if(vetor[c]%2==0):
        if(vetor[c]>mediaPar):
            print(vetor[c])
    else:
        if(vetor[c]>mediaImpar):
            print(vetor[c])
