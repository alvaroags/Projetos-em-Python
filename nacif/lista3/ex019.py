x=3
soma=1
for c in range(0,51):
    if(c%2==0):
        soma+= (-(1/(x**3)))
    else:
        soma+= (1/(x**3))
    x+=2
pi = (soma*32) ** (1/3)
print(pi)