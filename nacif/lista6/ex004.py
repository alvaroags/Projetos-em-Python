vetor = [0 for c in range(10)]
for c in range(10):
    vetor[c] = int(input())
N = int(input('valor de N'))
for c in range(10):
    if(N==vetor[c]):
        print(c)
        break
    elif(N!=vetor[9]):
        print('Não existe o numero na sequencia')