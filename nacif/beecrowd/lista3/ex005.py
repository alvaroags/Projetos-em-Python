num1,num2 = map(int,input().split(" "))
while(num1>0 and num2>0):
    soma=0
    if(num1<num2):
        for c in range(num1,num2+1):
            print(c)
            soma +=c
    else:
        for c in range(num2,num1+1):
            print(c)
            soma +=c
    print(f'Sum={soma}')
    num1 = int(input())
    num2 = int(input())