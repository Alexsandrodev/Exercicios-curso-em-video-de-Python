# Variaveis
dados = {}
pessoas = []
media = 0
soma_idade = 0

# Entradada de dados

while True:
    nome = input('Nome: ')
    sexo = input('Sexo: [F/M] ').strip().upper()[0]
    while sexo not in 'FM':
        sexo = input('Sexo: [F/M]').strip().upper()[0]       
    idade = int(input('idade: '))


# Tratamento de dados
    dados['nome'] = nome
    dados['sexo'] = sexo
    dados['idade'] = idade

    pessoas.append(dados.copy())
    dados.clear()

    resposta = input('Deseja continuar? [S/N]').strip().upper()[0]
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N]').strip().upper()[0]

    if resposta == 'N':
        break
    else:
        pass


for pessoa in pessoas:
    soma_idade += idade

media = soma_idade / len(pessoa)

# Saida de dados

print('-=-' * 30)
print(f'Foram registradas {len(pessoas)} pessoas.')
print(f'A media de idade das pessoas cadastradas é {media:.2f}.')
print('As mulheres cadastradas foram: ', end='')
for pessoa in pessoas:
    if pessoa['sexo'] == 'F':
        print(pessoa['nome'], end='. ')
        

print()
print(f'Pessoas acima da midia: ')

for pessoa in pessoas:
    if pessoa['idade'] > media:
        print(f'\n nome: {pessoa["nome"]}; idade: {pessoa["idade"]}; sexo: {pessoa["sexo"]}')

print('Programa encerrado...')