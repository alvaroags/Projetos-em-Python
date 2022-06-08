N = [0 for c in range(20)]
trocaVetor = [0 for c in range(20)]
for c in range(20):
    N[c] = int(input())
for c in range(20):
    trocaVetor[c] = N[19-c]
for c in range(20):
    print(f'N[{c}] = {trocaVetor[c]}')
