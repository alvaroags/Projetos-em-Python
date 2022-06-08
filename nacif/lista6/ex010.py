nota = []
nome = []
maior=0
menor=9999999999
for c in range(5):
    nota.append(int(input()))
    nome.append(str(input()))
    if(nota[c]>maior):
        maior = nota[c]
        indiceMaior = c
    if(nota[c]<menor):
        menor = nota[c]
        indiceMenor = c
print(f'Aluno = {nome[indiceMaior]}, nota = {nota[indiceMaior]}')
print(f'Aluno = {nome[indiceMenor]}, nota = {nota[indiceMenor]}')