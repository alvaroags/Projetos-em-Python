peso = float(input())
altura = float(input())
altura = altura/100
imc = peso/(altura*altura)
if(imc<20):
    print('ABAIXO DO PESO')
elif(20<=imc<25):
    print('PESO NORMAL')
elif(25<=imc<30):
    print('SOBREPESO')
elif(30<=imc<40):
    print('OBESO')
else:
    print('OBESO MÓRBIDO')
