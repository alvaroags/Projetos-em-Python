import math
otimo=0
bom=0
regular=0
ruim=0
pessimo=0
mediaRuim=0
idadeOtimo=0
idadeRuim=0
idadePessimo=0
for c in range(0,10):
    idade = int(input())
    opFilme = str(input())
    if(opFilme=='A'):
        otimo+=1
        if(idade>idadeOtimo):
            idadeOtimo = idade
    elif(opFilme=='B'):
        bom+=1
    elif(opFilme=='C'):
        regular+=1
    elif(opFilme=='D'):
        ruim+=1
        mediaRuim+=idade
        if(idade>idadeRuim):
            idadeRuim = idade
    elif(opFilme=='E'):
        pessimo+=1
        if(idade>idadePessimo):
            idadePessimo = idade
print('pessoas otimo = ', otimo)
print('diferença bom e regular = ', math.fabs(bom-regular))
print('media ruim = ', mediaRuim/ruim)
print('porcento pessimo = ',pessimo)
print('idade pessimo = ',idadePessimo)
print('diferença entre idade otimo e ruim = ', math.fabs(idadeOtimo-idadeRuim))