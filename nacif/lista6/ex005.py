nota = []
soma=0
for c in range(15):
    nota.append(float(input()))
for c in range(15):
    soma+=nota[c]
print(soma/15)