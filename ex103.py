# Funcões
def ficha(n='', g=''):
    if n == '':
        n = '<desconhecido>'

    if g == '':
        g = 0
        
    elif g == str:
        g = int(g)

    return f'O jogador {n} fez {g} gol(s) no campeonato'
# Programa principal

# Entrada de dados

nome = input('Nome do jogador: ')
gols = input('Número de gols: ')


print(ficha(nome, gols))