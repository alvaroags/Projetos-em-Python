num, num2 = map(int, input().split())
while num!=0 and num2!=0:
    soma = str(num + num2)
    nova = ''
    lista = list(soma)
    for c in range(len(soma)):
        if(lista[c]!='0'):
            nova = nova + lista[c]
    print(nova)
    num, num2 = map(int, input().split())
