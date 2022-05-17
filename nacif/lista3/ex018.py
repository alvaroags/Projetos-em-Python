x = 37
soma=0
for c in range(1,38):
    soma += (c*(c+1)) / x
    x-=1
print(f'SOMA = {soma:.2f}')