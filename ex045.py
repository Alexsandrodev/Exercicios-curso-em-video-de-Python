from random import choice

jogador = int(input('selecione [1] para Pedra, [2] para Tesoura e [3] para Papel: '))
computador = choice(['Pedra', 'Tesoura', 'Papel'])


if jogador == 1 and computador == 'Pedra':
    j = 'Pedra'
    print('\033[0;33mEmpate, os dois selecionaram {}\033[m'.format(j))

elif jogador == 1 and computador == 'Tesoura':
    j = 'Pedra'
    print('\033[0;32mO jogador ganhou, ele selecionou {} e o computador {}\033[m'.format(j, computador))

elif jogador == 1 and computador == 'Papel':
    j = 'Pedra'
    print('\033[0;31mO jogador perdeu,  ele selecionou {} e o computador {}\033[m'.format(j, computador))

elif jogador == 2 and computador == 'Tesoura':
    j = 'Tesoura'
    print('\033[0;33mEmpate, os dois selecionaram {}\033[m'.format(j))

elif jogador == 2 and computador == 'Papel':
    j = 'Tesoura'   
    print('\033[0;32mO jogador ganhou, ele selecionou {} e o computador {}\033[m'.format(j, computador))

elif jogador == 2 and computador == 'Pedra':
    j = 'Tesoura'   
    print('\033[0;31mO jogador perdeu,  ele selecionou {} e o computador {}\033[m'.format(j, computador))

elif jogador == 3 and computador == 'Papel':
    j = 'Papel'
    print('\033[0;33mEmpate, os dois selecionaram {}\033[m'.format(j))

elif jogador == 3 and computador == 'Pedra':
    j = 'Pepel'
    print('\033[0;32mO jogador ganhou, ele selecionou {} e o computador {}\033[m'.format(j, computador))

elif jogador == 3 and computador == 'Tesoura':
    j = 'Papel'
    print('\033[0;31mO jogador perdeu,  ele selecionou {} e o computador {}\033[m'.format(j, computador))
    