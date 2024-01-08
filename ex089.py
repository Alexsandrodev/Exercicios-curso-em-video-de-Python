# Variaveis
alunos = []
dados = []
notas = []
cont = 0

# loop infinito
while True:
# entrada de dados
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))

# Tratamento de dados  
    notas.append(nota1,)
    notas.append(nota2)
    dados.append(nome)
    dados.append(notas[:])
    alunos.append(dados[:])
    dados.clear()
    notas.clear()

    continuar = input('Registar mais alunos? [S/N] ').strip().lower()[0]
    while continuar not in 'ns':
        continuar = input('Registar mais alunos? [S/N]').strip().lower()[0]
    
    if continuar == 'n':
        break

print('-=-' * 30)

print(f'{"id":<3} {"Nome":<15} {"Média":<10}')
print('_' * 35)

for aluno in alunos:
    media = (aluno[1][0] + aluno[1][1]) / 2
    print(f'{cont:<3} {aluno[0]:<15} {media:<10}')

    cont += 1


while True:
    print('_' * 40)
    id_aluno = int(input('Deseja mostar a nota de qual aluno? (digite um número negativo para interomper) '))

    if id_aluno < 0:
        break

    print(f'Notas do {alunos[id_aluno][0]}: {alunos[id_aluno][1]}')

print('Programa encerrado!')