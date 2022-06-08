w1=1
w2=1
r=1
mediaT=0
cont=0
while(w1!=0 and w2!=0 and r!=0):
    w1, w2, r = map(int,input().split())
    mediaW1 = w1*(1+(r/30))
    mediaW2 = w2*(1+(r/30))
    media = (mediaW1+mediaW2)/2
    mediaT+= media
    cont+=1
    if(1<=media<13):
        print('Nao vai da nao')
    elif(13<=media<14):
        print('E 13')
    elif(14<=media<40):
        print('Bora, hora do show! BIIR!')
    elif(40<=media<=60):
        print('Ta saindo da jaula o monstro!')
    elif(media>60):
        print('AQUI E BODYBUILDER!!')
if(mediaT/cont) > 40:
    print('Aqui nois constroi fibra rapaz! Nao e agua com musculo!')
print(mediaT/cont)

        