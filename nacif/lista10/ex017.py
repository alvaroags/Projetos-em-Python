data = list(input().split('/'))
matrix = [['1', 'janeiro'], ['2', 'fevereiro'], ['3', 'março'], ['4', 'abril'], ['5', 'maio']]
print(matrix)
for c in range(1,5):
    if(data[1]==matrix[c][0]):
        print(f'Voce nasceu em {data[0]} de {matrix[c][1]} de {data[2]}')