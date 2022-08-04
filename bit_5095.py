import sys
def verificaERRO(tam, str1, str2):
    if(len(str1) != tam or len(str2) != tam or tam > 1000):
        print("ERRO")
        sys.exit()
    for i in range(tam):
        if((str1[i] != '0' and str1[i] != '1') or (str2[i] != '0' and str2[i] != '1')):
            print("ERRO")
            sys.exit()
def fAND(tam, str1, str2):
    for i in range(tam):
        if(str1[i] != str2[i]):
            str1[i] = '0'
    return str1
def fOR(tam, str1, str2):
    for i in range(tam):
        if(str1[i] == '1' or str2[i] == '1'):
            str1[i] = '1'
    return str1
def fXOR(tam, str1, str2):
    for i in range(tam):
        if(str1[i] != str2[i]):
            str1[i] = '1'
        else:
            str1[i] = '0'
    return str1
def fNOT(tam, str1):
    for i in range(tam):
        if(str1[i] == '1'):
            str1[i] = '0'
        else:
            str1[i] = '1'
    return str1
tam = int(input())
num1 = list(input().strip())
num2 = list(input().strip())
x = input().strip().split()
if(x[0] == "S1"):
    str1 = num1[:]
elif(x[0] == "S2"):
    str1 = num2[:]
if(x[2] == "S1"):
    str2 = num1[:]
elif(x[2] == "S2"):
    str2 = num2[:]
if(len(x) > 3):
    if(x[4] == "S1"):
        str3 = num1[:]
    elif(x[4] == "S2"):
        str3 = num2[:]
verificaERRO(tam, num1, num2)
i=1
while(i<4):
    if(x[i] == "AND"):
        str1 = list(''.join(fAND(tam, str1, str2)))
    elif(x[i] == "OR"):
        str1 = list(''.join(fOR(tam, str1, str2)))
    elif(x[i] == "XOR"):
        str1 = list(''.join(fXOR(tam, str1, str2)))
    elif(x[i] == "NAND"):
        str1 = list(''.join(fAND(tam, str1, str2)))
        str1 = list(''.join(fNOT(tam, str1)))
    elif(x[i] == "NOR"):
        str1 = list(''.join(fOR(tam, str1, str2)))
        str1 = list(''.join(fNOT(tam, str1)))
    elif(x[i] == "MOR"):
        str1 = list(''.join(fNOT(tam, str1)))
        str1 = list(''.join(fOR(tam, str1, str2)))
    else:
        print("ERRO")
        sys.exit()
    if(len(x)==3):
        break
    i+=2
    str2 = str3
for i in range(tam):
    print(str1[i], end="")
