nome = input()
for c in range(len(nome)+1):
    for i in range(c):
        print(f'{nome[i].upper()}', end='')
    print()