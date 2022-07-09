arquivo1 = input()
arquivo2 = input()
arquivo3 = input()
f3 = open(arquivo3, 'w')
with open(arquivo1) as f1, open(arquivo2) as f2:
    for c in range(50):
        f1Line1 = f1.readline()
        lista = f1Line1.split(' ')
        nota = (float(lista[0]) + float(lista[1])) / 2
        f2Line1 = f2.readline()
        nome = f2Line1.split('\n')
        f3.write(str(nome[0]) + str(" ") + str(nota))
        f3.write(str("\n"))
f1.close()
f2.close()
f3.close()