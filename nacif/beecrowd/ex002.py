import math
A,B,C = map(float,input().split())
condicao1 = ((math.fabs(B - C)) < A < (B + C))
condicao2 = ((math.fabs(A - C)) < B < (A + C))
condicao3 = ((math.fabs(A - B)) < C < (A + B))
if condicao1 and condicao2 and condicao3:
    print(f'Perimetro = {(A + B + C):.1f}')
else:
    print(f'Area = {((A + B) * C) / 2}')