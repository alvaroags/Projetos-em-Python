num = 1
soma=0
cont=0
while(num>=1):
    num = int(input())
    if(num%3==0):
        soma+=num
        cont+=1
print(soma/cont)