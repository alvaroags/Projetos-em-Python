a = float(input())
b = int(input())
soma=0
if(b>0):
    for c in range(0,b):
        soma += a
elif(b<0):
    for c in range(0,b,-1):
        soma -= a 
print(soma)