num = int(input())
soma=0
mult=1
while num>=0:
    if(num%2==0):
        soma += num
    else:
        mult *= num
    num = int(input())
print('SOMA DOS PARES =', soma)
print('PRODUTO DOS IMPARES =', mult)
