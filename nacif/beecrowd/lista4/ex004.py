A,G,RA,RG = map(float,input().split())
litroA = 10/A
litroG = 10/G
if(litroA * RA) > (litroG *RG):
    print('A')
else:
    print('G')
