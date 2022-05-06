tempo = float(input("DIGITE A QUANTIDADE DE TEMPO EM HORAS "))
vel = float(input("DIGITE A VELOCIDADE PERCORRIDA EM KM/H "))
distancia = tempo * vel
litros = distancia / 12
print("DISTANCIA PERCORRIDA: {:.2f}KM" .format(distancia))
print("QUANTIDADE DE LITROS DE COMBUSTÍVEL CONSUMIDO: {:.2f}L" .format(litros))