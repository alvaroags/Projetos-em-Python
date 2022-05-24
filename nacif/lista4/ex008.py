from re import I


x = int(input())
if(x<=1):
    funcao = 1
elif((x>1) and(x<=2)):
    funcao = 2
elif((x>2) and(x<=3)):
    funcao = x**2
else:
    funcao = x**3
print(funcao)