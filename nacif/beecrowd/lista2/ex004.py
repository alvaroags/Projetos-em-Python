A, B = map(int, input().split(' '))
if (B > A):
    horas = B - A
elif (A == B):
    horas = 24
else:
    horas = (24 - A) + B
print(f'O JOGO DUROU {horas} HORA(S)',)
