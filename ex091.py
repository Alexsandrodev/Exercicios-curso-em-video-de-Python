# Importações
from random import randint
from time import sleep
from operator import itemgetter

# Variaveis e entrada de dados
cont = 1
jogo = {'Jogador1': randint(1, 6), 
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6) ,       
}
ranking = {}

# Tratamento de dados e saida de dados
print('Valores sorterador..')

for k, v in jogo.items():
    print(f'    O {k} tirou {v} no dado.')
    sleep(0.5)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('Ranking')

for k, v in enumerate(ranking):
    print(f'    {k + 1}° lugar: {v[0]} com {v[1]}')
    sleep(1)

print('Parabens aos vencedores!!')