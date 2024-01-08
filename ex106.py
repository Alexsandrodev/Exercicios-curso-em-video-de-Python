# Funções
def titulo(msg):

    print('~' * (len(msg) + 4))
    print(f'  {msg}')
    print('~' * (len(msg) + 4))

def ajuda_comando(hp):

    return help(hp)

# Programa principal

while True:
    titulo('Sistema de ajuda PyHelp.')
    comando = input('Função ou Biblioteca: ')

    if comando == 'fim':
        titulo('Programa encerrado')
        break

    titulo(f'Acessando o manual do comando {comando}')

    print(ajuda_comando(comando))