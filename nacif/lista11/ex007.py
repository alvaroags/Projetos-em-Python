arquivo1 = input()
arquivo2 = input()
nome = input()
notaNova = input()
with open(arquivo1, 'r') as f1, open(arquivo2, 'w') as f2:
    x = f1.read()
    x = x.replace(nome, notaNova)
    f2.write(x)