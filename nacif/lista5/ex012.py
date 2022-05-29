import math
x = float(input())
sinal=1
seno=0
x = x * (math.pi / 180)
print(x)
for c in range(1,30,2):
    fat=1
    for i in range(1,c+1):
        fat *= i 
    seno += (((x**c)/ fat)*sinal)
    sinal*=-1
print(seno)