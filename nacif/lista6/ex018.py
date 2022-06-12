from re import I


conta = []
saldo = []
msg = ['positivo', 'negativo']
indice = 0
soma=0
negativo=0
while True:
    conta.append(int(input()))
    if(conta[indice]>=0):
        saldo.append(float(input()))
        soma+=saldo[indice]
        indice+=1
    else:
        break
for c in range(indice):
    if(saldo[c]>=0):
        print(f'{conta[c]} {saldo[c]} positivo')
    else:
        print(f'{conta[c]} {saldo[c]} negativo')
        negativo+=1
print(negativo)
print(indice)
print(soma)
print(((negativo/indice) * 100))