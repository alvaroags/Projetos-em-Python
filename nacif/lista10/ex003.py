lista = []
soma = 0 
for c in range(5):
    lista.append(int(input()))
    soma+=lista[c]
media = soma/5
menorDist = 0
idMenor = 0
for c in range(5):
    if(lista[c]>=media):
        dif = lista[c]-media
    else:
        dif = media-lista[c]
    if menorDist == 0 or menorDist>dif:
        menorDist = dif
        idMenor = c
print(media)
print(lista[idMenor])