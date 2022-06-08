s=0
denominador = 1
for c in range(1,40,2):
    s+= c/denominador
    denominador *= 2
print(f'{s:.2f}')