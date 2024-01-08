# Variaveis
jogador = {}
gols = []
cont = 1

# Entrada de dados

nome = input('Nome do Jogador: ')
Partidas  = int(input(f'Partidas jogadas por {nome}: '))

for c in range (1, Partidas +1):
    gols.append(int(input(f'Gols na {c}° partida: ')))

# tratamento de dados

jogador['nome'] = nome
jogador['gols'] = gols[:]
jogador['total'] = sum(jogador['gols'])

print('-=-' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas' )
print('-=-' * 30)

for g in jogador['gols']:
    print(f'    Na {cont}° partida, fez {g} gols')
    cont += 1

print(f'E fez um total de {jogador["total"]} gols')