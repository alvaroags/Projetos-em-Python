import sys
def verificaERRO(tam, str1, str2, str3):
    if(len(str1) != tam or len(str2) != tam  or len(str3) != tam or tam > 1000):
        print("ERRO")
        sys.exit()
    for i in range(tam):
        if((str1[i] != '0' and str1[i] != '1') or (str2[i] != '0' and str2[i] != '1') or(str3[i] != '0' and str3[i] != '1')):
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
str = []
tam = int(input())
num1 = list(input().strip())
num2 = list(input().strip())
num3 = list(input().strip())
x = input().strip().split()
for i in range(0, len(x),2):
    if(x[i] == "S1"):
        str.append(num1[:])
    elif(x[i] == "S2"):
        str.append(num2[:])
    elif(x[i] == "S3"):
        str.append(num3[:])
verificaERRO(tam, num1, num2, num3)
id=0
for i in range(1, len(x), 2):
    id+=1
    if(x[i] == "AND"):
        str[0] = list(''.join(fAND(tam, str[0], str[id])))
    elif(x[i] == "OR"):
        str[0] = list(''.join(fOR(tam, str[0], str[id])))
    elif(x[i] == "XOR"):
        str[0] = list(''.join(fXOR(tam, str[0], str[id])))
    elif(x[i] == "NAND"):
        str[0] = list(''.join(fAND(tam, str[0], str[id])))
        str[0] = list(''.join(fNOT(tam, str[0])))
    elif(x[i] == "NOR"):
        str[0] = list(''.join(fOR(tam, str[0], str[id])))
        str[0] = list(''.join(fNOT(tam, str[0])))
    elif(x[i] == "MOR"):
        str[0] = list(''.join(fNOT(tam, str[0])))
        str[0] = list(''.join(fOR(tam, str[0], str[id])))
    else:
        print("ERRO")
        sys.exit()
for i in range(tam):
    print(str[0][i], end="")
