from concurrent.futures.process import _MAX_WINDOWS_WORKERS
from smtpd import MailmanProxy


A = int(input())
B = int(input())
C = int(input())
if (A > B) and (A > C):
    if(C > B):
        print(A,C,B)
    else:
        print(A,B,C)
elif (B > A) and (B > C):
    if(A > C):
        print(B,A,C)
    else:
        print(B,C,A)
elif (C > A) and (C > A):
    if(A > B):
        print(C,A,B)
    else:
        print(C,B,A)