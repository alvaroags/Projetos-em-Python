nome = input()
qtCarros = int(input())
valorVendas = 0
for c in range(0,qtCarros):
    valorVendas += float(input('valor carros vendidos: ')) * 0.05
salario = 500 + (qtCarros*50) + valorVendas
print(f'SALARIO DO VENDEDOR =',salario)

