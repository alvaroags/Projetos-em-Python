n = int(input())
s=1
for c in range(0,n):
    if(c%3==0):
        print(s)
        s+=1
    else:
        print(s+2)
