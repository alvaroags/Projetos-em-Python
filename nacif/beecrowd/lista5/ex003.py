soma=0
cont=0
while True:
    try:
        nome = str(input())
        dist = float(input())
        soma += dist
        cont+=1
    except:
        break
print(f'{soma/cont:.1f}')