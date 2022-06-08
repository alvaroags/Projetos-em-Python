a = int(input('valor de a:'))
vetor = []
prod = [0 for x in range(5)]
for c in range(0,5):
    num = int(input('valor de num:'))
    vetor.append(num)
    prod[c] = vetor[c]*a
for c in range(0,5):
    if(prod[c]%2==0):
        print(prod[c],'Par')
    else:
        print(prod[c],'Impar')