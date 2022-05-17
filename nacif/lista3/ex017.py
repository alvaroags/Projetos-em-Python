soma=0
x=1
for c in range(1,51):
    soma += x/c
    if(c!=50):
        x+=2
print(f'SOMA = {soma:.2f}')
