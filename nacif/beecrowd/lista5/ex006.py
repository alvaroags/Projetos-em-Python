n=1
while(n!=0):
    n = int(input())
    if(n!=0):
        ri = list(map(int,input().split()))
        mary=0
        john=0
        for c in ri:
            if(c == 0):
                mary +=1
            elif(c == 1):
                john +=1
        print(f'Mary won {mary} times and John won {john} times')