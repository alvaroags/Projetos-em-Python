idade = int(input())
if(idade<16):
    print('NÃO ELEITOR')
elif((idade>=18) and (idade<=65)):
    print('VOTO OBRIGATÓRIO')
else:
    print('VOTO FACULTATIVO')