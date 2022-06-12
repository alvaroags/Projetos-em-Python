id = []
valor = []
indice = 0
soma = 0
while True:
    id.append(int(input(' ')))
    if(id[indice]>=0):
        valor.append(float(input(' ')))
        soma+=valor[indice]
        indice+=1
    else:
        break
print(soma/indice)