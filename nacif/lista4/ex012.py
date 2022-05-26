soma=0
for c in range (0,6):
     soma += float(input ())
if (soma /6) >= 7:
    print('Aprovado')
elif (soma/6) <=3:
    print('Reprovado')
else:
    print ('Em exame')