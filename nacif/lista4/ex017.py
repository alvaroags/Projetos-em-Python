n1 = int(input())
n2 = int(input())
n = int(input())
if(n>3):
    print(n1)
    print(n2)
    for c in range(0,n):
        x = n1 + n2
        n1 = n2
        n2 = x
        print(x)