n = int(input())
S=0
for c in range(1,n+1):
    S += 1/(c*c)
print(f'{S:.2f}')