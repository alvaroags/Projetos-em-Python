num1 = int(input())
num2 = int(input())
n = int(input())
if(n>=3):
    print(num1)
    print(num2)
    for c in range(3,n):
        if(c%2==0):
            aux = num2
            num2 = num2 - num1
            num1 = aux
        else:
            aux = num2
            num2 = num2 + num1
            num1 = aux
        print(num2)
