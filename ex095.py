# Variaveis
jogadores =  []
jogador = {}
gols = []
cont = 1
indice = 0

# Entrada de dados
while True:
    nome = input('Nome do Jogador: ')
    Partidas  = int(input(f'Partidas jogadas por {nome}: '))

    for c in range (1, Partidas +1):
        gols.append(int(input(f'Gols na {c}° partida: ')))

# tratamento de dados

    jogador['nome'] = nome
    jogador['gols'] = gols[:]
    jogador['total'] = sum(jogador['gols'])
    jogadores.append(jogador.copy())
    jogador.clear()

    continuar = input('Registar mais jogadores? [S/N] ').strip().upper()[0]

    print('_' * 70)
    while continuar not in 'SN':
        continuar = input('Registar mais jogadores? [S/N] ').strip().upper()[0]

    if continuar == 'N':
        break

print(f'{"id":<5} {"nome":<20} {"gols":<30} {"total":<7}')

for jogador in jogadores:
    print(f'''{f"{indice}":<5} {f"{jogador['nome']}":<20} {f"{jogador['gols']}":<30} {f"{jogador['total']}":<7}''')
    indice += 1


while True:
    num = int(input('digite o id de qual jogador você deseja ver as estatisicas: '))
    
    for g in jogadores[num]['gols']:
        print(f'    Na {cont}° partida, fez {g} gols')
        cont += 1

    print(f'E fez um total de {jogador["total"]} gols')