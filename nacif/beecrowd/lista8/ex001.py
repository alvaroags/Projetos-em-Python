vetorPar = []
vetorImpar = []
contPar = 0
contImpar = 0
for c in range(15):
    num =  int(input())
    if(num%2==0):
        vetorPar.append(num)
        contPar+=1
        if(contPar==5):
            for x in range(5):
                print(f'par[{x}] = {vetorPar[x]}')
                contPar = 0
            vetorPar = []
    else:
        vetorImpar.append(num)
        contImpar+=1
        if(contImpar==5):
            for x in range(5):
                print(f'impar[{x}] = {vetorImpar[x]}')
                contImpar = 0
            vetorImpar = []
for c in range(contImpar):
    print(f'impar[{c}] = {vetorImpar[c]}')
for c in range(contPar):
    print(f'par[{c}] = {vetorPar[c]}')