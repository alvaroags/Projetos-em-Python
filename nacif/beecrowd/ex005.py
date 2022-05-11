S = float(input())
if(S>=0) and (S<=400):
    NS = S * 1.15
    R = S * 0.15
    P = 15
elif (S>400) and (S<=800):
    NS = S * 1.12
    R = S * 0.12
    P = 12
elif (S>800) and (S<=1200):
    NS = S * 1.10
    R = S * 0.10
    P = 10
elif (S>1200) and (S<=2000):
    NS = S * 1.07
    R = S * 0.07
    P = 7
else:
    NS = S * 1.04
    R = S * 0.04
    P = 4
print(f'Novo salario: {NS:.2f}\nReajuste ganho: {R:.2f}\nEm percentual: {P}%')