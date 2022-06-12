nome = []
real = []
dolar = []
for c in range(1):
    nome.append(str(input()))
    dolar.append(float(input()))
    real.append(dolar[c]/5)
for c in range(1):
    print(f'{nome[c]} {dolar[c]} {real[c]}')