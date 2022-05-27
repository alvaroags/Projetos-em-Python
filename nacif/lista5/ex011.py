a = int(input())
b = int(input())
if((a and b) > 0):
    if(b>a):
        print(a)
    else:
        while(b>0):
            a-=b
        print(a)