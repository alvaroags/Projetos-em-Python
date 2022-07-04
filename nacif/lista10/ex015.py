frase = list(input())
frase2 = list(input())
idlista = [-1]
cont=0
if(len(frase)==len(frase2)):
    for c in range(len(frase)):
        for i in range(len(frase)):
            if(frase[c]==frase2[i] and i not in idlista):
                idlista.append(i)
                cont+=1
if(cont==len(frase)):
    print('anagrama')
else:
    print('nao é anagrama')