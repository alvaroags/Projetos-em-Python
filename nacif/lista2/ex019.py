idade = int(input())
peso = int(input())
if((idade>=12) and (peso>60)):
    gotas = 500 / 25
elif((idade>=12) and (peso<=60)):
    gotas = 875 / 25
else:
    if((peso>=5) and (peso<=9)):
        gotas = 125 / 25
    elif((peso>=9) and (peso<=16)):
        gotas = 250 / 25
    elif((peso>=16) and (peso<=24)):
        gotas = 275 / 25
    elif((peso>=24) and (peso<=30)):
        gotas = 500 / 25
    elif(peso>30):
        gotas = 750 / 25
print(f'VOCE PRECISA TOMAR {gotas:.0f} gotas')
