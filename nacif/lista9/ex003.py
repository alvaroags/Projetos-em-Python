matrix = [[0 for c in range(3)] for i in range(3)]
prod=1
for c in range(3):
    for i in range(3):
        matrix[c][i] = int(input())
for c in range(3):
    for i in range(3):
        if(c>i):
            prod*=matrix[c][i]
print(prod)