import random
import re
arquivo1 = input()
arquivo2 = input()
arquivo3 = input()
f1 = open(arquivo1, 'r')
f2 = open(arquivo2, 'w')
f3 = open(arquivo3, 'w')
for texto in f1:
    aux = texto
    ip = re.split("[.\n]", aux)
    if((0<int(ip[0])<=255) and (0<=int(ip[1])<=255) and (0<=int(ip[2])<=255) and (0<=int(ip[2])<=255)):
        f2.write(texto)
    else:
        f3.write(texto)
