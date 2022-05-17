mascSim=0
mascNao=0
femSim=0
femNao=0
for c in range(0,5):
    sexo = int(input('DIGITE 1 PARA MASCULINO E 2 PARA FEMININO '))
    like = int(input('DIGITE 1 SE VOCE GOSTOU DO PRODUTO E 2 PARA NÃO '))
    if(sexo==1):
        if(like==1):
            mascSim += 1
        else:
            mascNao += 1
    else:
        if(like==1):
            femSim += 1
        else:
            femNao += 1
print(f'\nPESSOAS QUE RESPONDERAM SIM {mascSim+femSim}')
print(f'PESSOAS QUE RESPONDEREM NÃO {mascNao+femNao}')
print(f'PORCENTAGEM DE MULHER QUE RESPONDERAM SIM {(femSim / (femNao+femSim)) * 100:.2f}%')
print(f'PORCENTAGEM DE HOMENS QUE RESPONDERAM NÃO {((mascNao)/ (mascNao+mascSim)) * 100:.2f}%')