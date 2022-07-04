frase = input().split(" ")
i=0
while True:
    try:
        p = frase[i]
        i+=1
    except:
        break
print(i)