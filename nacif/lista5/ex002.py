saldo = float(input())
if(saldo<=500):
    print('NENHUM CRÉDITO')
elif(500<saldo<=1000):
    print(f'VALOR DO CRÉDITO = {saldo*0.3:.2f}')
elif(1000<saldo<=3000):
    print(f'VALOR DO CRÉDITO = {saldo*0.4:.2f}')
else:
    print(f'VALOR DO CRÉDITO = {saldo*0.5:.2f}')