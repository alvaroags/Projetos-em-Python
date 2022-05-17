num = int(input())
somaPar=0
contPar=0
somaImpar=0
contImpar=0
maiorPar=0
menorImpar=0
while num>0:
    if(num%2==0):
        somaPar+=num
        contPar+=1
        if(num>maiorPar) or (contPar==1):
            maiorPar = num
    else:
        somaImpar+=num
        contImpar+=1
        if(num<menorImpar) or (contImpar==1):
            menorImpar = num
    num = int(input())
print(f'MEDIA DOS PARES = {(somaPar/contPar):.2f} E MAIOR PAR {maiorPar}')
print(f'MEDIA DOS IMPARES = {(somaImpar/contImpar):.2f} E MENOR IMPAR {menorImpar}')