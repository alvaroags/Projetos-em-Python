N = int(input())
if(N < 10000):
    for c in range(1,10000):
        if(c % N ==2):
            print(c)