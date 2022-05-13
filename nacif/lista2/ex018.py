peso = float(input())
planeta = int(input())
if(planeta == 1):
    peso = peso * 0.37
elif(planeta == 2):
    peso = peso * 0.88
elif(planeta == 3):
    peso = peso * 0.38
elif(planeta == 4):
    peso = peso * 2.64
elif(planeta == 5):
    peso = peso * 1.15
elif(planeta == 6):
    peso = peso * 1.17
print(f'O NOVO PESO É {peso:.2f}')