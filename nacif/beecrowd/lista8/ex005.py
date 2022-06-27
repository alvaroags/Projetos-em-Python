
while True:
    try:
        n = int(input())
        matrix = [[0 for c in range(n)] for i in range(n)]
        for c in range(n):
            for i in range(n):
                if((n-1)-c)==i:
                    matrix[c][i] = 2
                elif(c==i):
                    matrix[c][i] = 1
                else:
                    matrix[c][i] = 3
        for c in range(n):
            for i in range(n):
                print(f'{matrix[c][i]}', end='')
            print()
    except EOFError:
        break
