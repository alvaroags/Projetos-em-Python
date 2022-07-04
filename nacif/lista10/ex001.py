from random import randint
a = []
b = [0 for c in range(6)]
for c in range(10):
    a.append(randint(1,6))
for c in range(10):
    b[a[c]-1] = b[a[c]-1]+1
print(a)
print(b)