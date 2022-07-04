frase = input()
l = list(frase)
frase2 = [0 for c in range(len(frase))]
for c in range(len(frase)):
    if(l[c]==' '):
        l[c] = '#'
frase = ' '.join(l)
print(frase)