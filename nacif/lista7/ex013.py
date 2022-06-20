vetor1 = [0 for c in range(5)]
vetor2 = [0 for c in range(5)]
i=0
while i<5:
    num = int(input())
    rep = 0
    for c in range(5):
        if(num==vetor1[c]):
            rep = 1
    if(rep==0):
        vetor1[i] = num
        i+=1
for c in range(5):
    vetor2[c] = int(input())
x = int(input('X = '))
for c in range(5):
    if(vetor1[c]==x):
        print(vetor1[c])
        print(vetor2[c])
        break