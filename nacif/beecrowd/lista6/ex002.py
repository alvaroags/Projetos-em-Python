N = []
num = int(input())
for c in range(10):
    N.append(num)
    num*=2
for c in range(10):
    print(f'N[{c}] = {N[c]}')