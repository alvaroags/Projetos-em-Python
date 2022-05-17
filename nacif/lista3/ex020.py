X = int(input())
x=25
soma=0
for c in range(1,26):
    if(c%2==0):
        soma+= (-((X**x) / c))
    else:
        soma+= ((X**x) / c)
    x-=1
print(f'soma = {soma:.2f}')