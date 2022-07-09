import random
N = int(input())
nome = ['Alvaro ', 'José ', 'Pedro ', 'João ', 'Mateus ']
sobrenome = ['Gomes ', 'Pereira ', 'Silva ', 'Neto ', 'Almeida ']
nomeArquivo = input()
arquivoNomes = open(nomeArquivo, 'w')
for c in range(N):
    arquivoNomes.write(str(nome[random.randint(0,4)]))
    arquivoNomes.write(str(sobrenome[random.randint(0,4)]))
    arquivoNomes.write(str(random.randint(15,60)) + str(' '))
    arquivoNomes.write(str(round(random.uniform(1.5,2.2), 2)))
    arquivoNomes.write('\n')
arquivoNomes.close()