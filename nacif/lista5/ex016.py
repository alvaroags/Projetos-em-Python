mediaIdade=0
nome='A'
alto=0
cont=0
pesada=0
while(nome!='@'):
    nome = str(input())
    if(nome!='@'):
        sexo = str(input())
        idade = int(input())
        peso = float(input())
        altura = float(input())
        if(sexo=='M'):
            if(altura>alto):
                alto = altura
        if(sexo=='F'):
            if(peso>pesada):
                pesada = peso
        mediaIdade+=idade
        cont+=1
print(alto)
print(pesada)
print(mediaIdade/cont)