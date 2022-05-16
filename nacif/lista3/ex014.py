cand1 = 0
cand2 = 0
cand3 = 0
cand4 = 0
votoB = 0
votoN = 0
voto = 1
cont = 0
while voto>0 and voto<=6:
    voto = int(input())
    cont += 1
    if(voto==1):
        cand1+=1
    elif(voto==2):
        cand2+=1
    elif(voto==3):
        cand3+=1
    elif(voto==4):
        cand4+=1
    elif(voto==5):
        votoN+=1
    elif(voto==6):
        votoB+=1
porc = ((votoB+votoN) / cont) * 100
print(f' CANDITADO 1 = {cand1} \n CANDITADO 2 = {cand2} \n CANDITADO 3 = {cand3} \n CANDITATO 4 = {cand4} \n VOTO BRANCO = {votoB} \n VOTO NULO = {votoN} \n PERCENTUAL DE VOTOS = {porc:.2f}')