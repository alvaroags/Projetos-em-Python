dividendo = int(input())
divisor = int(input())
quociente = dividendo / divisor
resto = dividendo % divisor
if divisor == 0:
    print('Divisão não permitida')
else:
    print(f'QUOCIENTE: {quociente:.0f}\nRESTO: {resto}')