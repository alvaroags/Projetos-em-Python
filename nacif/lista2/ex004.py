idade = int(input())
if idade>365:
    ano = idade / 365
    mes = (idade % 365) / 30
    dias = ((idade % 365) % 30)
elif idade>30:
    ano = 0
    mes = idade / 30
    dias = idade % 30
else:
    ano = 0
    mes = 0
    dias = idade 
print(f'A PESSOA TEM {ano:.0f} anos {mes:.0f} meses e {dias} dias')
