arquivo1 = input()
arquivo2 = input()
f1 = open(arquivo1, 'r')
f2 = open(arquivo2, 'w')
for texto in f1:
    if(texto[0:2]!="//"):
        f2.write(texto)
f1.close()
f2.close()