n = int(input())
if(0<n<46):
    t1=0
    t2=1
    print('{} {}' .format(t1,t2,), end=' ')
    for c in range(3,n+1):
        t3 = t2 + t1
        if(c!=n):
            print('{}' .format(t3), end='')
        else:
            print(t3)
        t1 = t2
        t2 = t3
