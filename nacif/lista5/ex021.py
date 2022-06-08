primo=0
n = int(input())
for c in range(1,n+1):
    contDivisores=0
    for i in range(1,c+1):
        if(c%i==0):
            contDivisores+=1
    if(contDivisores<=2):
        primo+=1
print(c)
print(i)
print(primo)
