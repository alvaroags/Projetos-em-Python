salario = float(input())
if(salario<=2000):
    print('Isento')
else:
    if(salario>2000 and salario<=3000):
        imposto = (salario - 2000) * 0.08
    elif (salario>3000 and salario<=4500):
        imposto = ((salario - 3000) * 0.18) + (1000*0.08)
    elif (salario>4500):
        imposto = ((salario - 4500) * 0.28) + (1000*0.08) + (1500*0.18)
    print(f'R$ {imposto:.2f}')
