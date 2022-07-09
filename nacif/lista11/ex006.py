import random
arquivo1 = input()
f1 = open(arquivo1, 'w')
for c in range(50):
    f1.write(str(round(random.uniform(0,100), 1))+ str(' ')+ str(round(random.uniform(0,100), 2))+ str('\n'))