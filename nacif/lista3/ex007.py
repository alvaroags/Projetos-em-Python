contPar = 0
contImpar = 0
for c in range(0,200):
    num = int(input())
    if(num%2 == 0):
        contPar+=1
    else:
        contImpar+=1
print('NUMEROS PARES =',contPar)
print('NUMEROS IMPARES =',contImpar)
