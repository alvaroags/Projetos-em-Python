ano = int(input('ANOS: '))
meses = int(input('MESES: '))
dias = int(input('DIAS: '))
idade = (ano*365)+(meses*30)+dias
print(f'A PESSOA TEM {idade} dias de vida')
if ano>=60:
    print('A PESSOA É IDOSA')
elif ano>=18:
    print('A PESSOA É ADULTA')
elif ano>=12:
    print('A PESSOA É ADOLESCENTE')
elif ano>=3:
    print('A PESSOA É CRIANÇA')
else:
    print('A PESSOA É BEBE')