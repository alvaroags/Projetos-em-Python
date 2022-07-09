qtdNumeros = int(input())
nomeArquivo = input()
arquivosNumeros = open(nomeArquivo, 'w')
for i in range(qtdNumeros):
    arquivosNumeros.write(str(input()))
    arquivosNumeros.write('\n')
arquivosNumeros.close()