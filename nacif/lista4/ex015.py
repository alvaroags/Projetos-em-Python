contD=0
contF=0
for c in range(0,10):
    n = int(input())
    if(10<=n<=20):
        contD+=1
    else:
        contF+=1
print(contD)
print(contF)