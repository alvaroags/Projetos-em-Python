x = []
n = int(input())
x = input().split(" ")
for c in range(n):
    x[c] = int(x[c])
menor=0
for c in range(n):
    if(x[c]<menor or c==0):
        menor = x[c]
        idmenor = c
print(f'Menor valor: {menor}')
print(f'Posicao: {idmenor}')