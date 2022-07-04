frase = list(input())
frase2 = list(input())
print(len(frase))
i=0
if(len(frase)==len(frase2)):
    for c in range(len(frase)):
        if(frase[c]==frase2[len(frase)-1-c]):
            i=1
        else:
            i=0
if i==1:
    print('palindroma')
else:
    print('nao é palindroma')