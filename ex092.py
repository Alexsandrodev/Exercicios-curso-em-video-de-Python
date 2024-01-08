from datetime import date
# variaveis
dados = {}
ano_atual = date.today().year
# entrada de dados

nome = input('Nome: ')
data = int(input('Data de nacimento: '))
idade = ano_atual - data
carteira = int(input('Carteira de trabalho (0 Não tem): '))

dados['nome'] = nome
dados['idade'] = idade
dados['ctps'] = carteira

if carteira != 0:
    contratação = int(input('Ano de contratação: '))
    salario = float(input('Sálario: R$'))
    anos_trabalhados = ano_atual - contratação

    aposentadoria = idade + 35 - anos_trabalhados

    dados['contratação'] = carteira
    dados['sálario'] = salario
    dados['aposentadoria'] = aposentadoria

print('-=-' * 30)

for k, v in dados.items():
    print(f'O {k} tem o valor {v}')