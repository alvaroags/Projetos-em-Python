matrix = [[0 for c in range(4)]for i in range(4)]
gasto = []
for c in range(4):
    for i in range(2):
        matrix[c][i] = input()
for c in range(4):
    gasto.append((100//float(matrix[c][1])) * 3.5)
    if(c==0 or gasto[c]<menor):
        menor=gasto[c]
        idEco = c
    print(f'{matrix[c][0]} gasta {gasto[c]}')
print(f'{matrix[idEco][0]} é o mais economico')