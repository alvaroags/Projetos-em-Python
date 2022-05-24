A,B,C = map(int, input().split())
if(A>B and B<=C):
    print(':)')
elif(B>A and B>=C):
    print(':(')
elif(B>A and C>B):
    if(B-A)>(C-B):
        print(':(')
    elif((B-A)<=(C-B)):
        print(':)')
elif(B<A and C<B): 
    if((B-A)<(C-B)):
        print(':)')
    elif((B-A)>=(C-B)):
        print(':(')
elif(B==A) and (C>=B):
    print(':)')
elif(B==A) and (C<B):
    print(':(')