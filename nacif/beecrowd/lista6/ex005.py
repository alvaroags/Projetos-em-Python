fib = [0 for c in range(60)]
for c in range(60):
    if(c<2):
        fib[c] = c
    else:
        fib[c] = fib[c-1] + fib[c-2]
T = int(input())
for c in range(T):
    N = int(input())
    if(0<=N<=60):
        print(f'Fib({N}) = {fib[N]}')