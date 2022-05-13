bola = int(input())
dinheiro = float(input())
if(bola==0):
    porc = 0.05
elif(bola==1):
    porc = 0.25
elif(bola==2):
    porc = 0.10
elif(bola==3):
    porc = 0.07
elif(bola==4):
    porc = 0.08
elif(bola==5):
    porc = 0.05
elif(bola==6):
    porc = 0.15
elif(bola==7):
    porc = 0.12
elif(bola==8):
    porc = 0.03
elif(bola==9):
    porc = 0.10
print(f'O DINHEIRO GANHO É: {dinheiro*porc:.2f}')
