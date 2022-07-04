nome = list(input())
nome2 = list(0 for c in range(len(nome)))
for c in range(len(nome)):
    nome2[c] = nome[len(nome)-1-c]
nome = ''.join(nome2)
print(nome.upper())