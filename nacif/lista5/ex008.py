c=0
num=1
maior=0
menor=9999999
while(num!=-1):
    num = int(input())
    if(((num>maior) or (c==0)) and num>=0):
        maior = num
    if(((num<menor) or (c==0)) and num>=0):
        menor = num
    c+=1
print(maior)
print(menor)