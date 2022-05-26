qt = int(input())
cont=0
for c in range(0,qt+1):
    massa = float(input())
    while(massa>=0.1):
        massa = massa*0.75
        cont+=30
    print(cont)
    