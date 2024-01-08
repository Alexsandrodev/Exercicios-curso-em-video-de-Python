# variaveis
pessoas = []
dados = []
cont = 0
maior_peso = 0
pessoas_pesadas = []
menor_peso = 0
pessoas_leves = []


# Loop para entrada de dados
while True:
    nome = input('nome: ')
    pessoa = float(input('Peso (Kg): '))
    dados.append(nome)
    dados.append(pessoa)
    pessoas.append(dados[:])
    dados.clear()

    while True:
        continuar = input('Dejesa registar mais alguem? [S/N] ').strip().lower()[0]

        if continuar in 'sn':
            break

    print('-=-' * 30)
    if continuar == 'n':
        break


# Tratamento dos dados
for pessoa in pessoas:
    if cont == 0:
        maior_peso = menor_peso =  pessoa[1]

    else:
        if maior_peso < pessoa[1]:
            maior_peso = pessoa[1]

        if menor_peso > pessoa[1]:
            menor_peso = pessoa[1]
    
    cont += 1

for pessoa in pessoas:
    if pessoa[1] == maior_peso:
        pessoas_pesadas.append(pessoa[0])

    if pessoa[1] == menor_peso:
        pessoas_leves.append(pessoa[0])


cont = 1
# Saida de dados
print(f'{len(pessoas)} pessoas foram cadastradas.')

print(f'O maior peso foi de {maior_peso:.1f}. Peso de ', end='')
for p in pessoas_pesadas:
    if cont != len(pessoas_pesadas):
        print(f'{p}, ', end='')

    else:
        print(p)

    cont += 1

cont = 1
print(f'O menor peso foi de {menor_peso:.1f}. Peso de ', end='')
for p in pessoas_leves:
    if cont != len(pessoas_leves):
        print(f'{p}, ', end='')

    else:
        print(p)

    cont += 1