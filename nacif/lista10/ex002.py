from asyncio.windows_events import NULL


lista1 = []
lista2 = []
lista3 = []
for c in range(4):
    lista1.append(int(input()))
for c in range(6):
    lista2.append(int(input()))
for c in range(4):
    lista3.append(lista1[c])
    lista3.append(lista2[c])
lista3 = lista3 + lista2[4:6]
print(lista3)