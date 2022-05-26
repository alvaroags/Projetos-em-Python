valor = int(input ())
if valor < 10:
    venda = valor * 1.7
elif 10 >= valor > 30:
    venda = valor * 1.5
elif 30>= valor > 50:
    venda = valor * 1.4
else:
    venda = valor * 1.3
print(f'valor de venda = {venda:.2f}')