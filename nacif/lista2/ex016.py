mes = int(input())
if((mes<1) or (mes>12)):
    print('MES INVALIDO')
else:
    if((mes>=1) and (mes<=3)):
        print('primeiro trimestre')
    elif((mes>=4) and (mes<=6)):
        print('segundo trimestre')
    elif((mes>=7) and (mes<=9)):
        print('terceiro trimestre')
    elif((mes>=10) and (mes<=12)):
        print('quarto trimestre')