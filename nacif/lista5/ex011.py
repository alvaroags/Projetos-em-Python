a = int(input())
b = int(input())
if((a and b) > 0):
    if(b>a):
        print(a)
    else:
        while(a>=b):
            a = a - b
        print(a)