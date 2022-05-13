for c in range(0,5):
    num = int(input())
    if((num>maior) or (c==0)):
        maior = num
    if((num<menor) or (c==0)):
        menor = num
print(maior)
print(menor)