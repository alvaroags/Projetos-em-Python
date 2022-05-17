num1 = int(input())
num2 = int(input())
soma=0
if(num1>num2):
    for c in range(num1,num2,-1):
        if((c%2 ==1) and ((c != num1) and (c != num2))):
            soma +=c
else:
    for c in range(num1,num2):
        if((c%2 ==1) and ((c != num1) and (c != num2))):
            soma += c
print(soma)