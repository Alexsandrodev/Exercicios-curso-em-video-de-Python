# variaveis
aluno = {}

nome = input('Nome do aluno: ')
media = float(input(f'média do {nome}: '))

aluno['Nome'] = nome
aluno['Media'] = media

if media >= 7:
    aluno['Situação'] = 'Aprovado'
elif media >=5:
    aluno['Situação'] = 'Recuperação'
else:    
    aluno['Situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f'O {k} é igual a {v}')