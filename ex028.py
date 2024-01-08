from random import randint
from time import sleep

Computador = randint(0, 5)

print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhalo...')
print('-=-' * 20)

Jogador = int(input('Em qual número eu pendei? '))

print('Processando...')
sleep(2)

if Computador == Jogador:
    print('PARABENS! você conseguiu vencer!')
else:
    print(f'PERDEU! Eu pensei no numero {Computador} e não no {Jogador}')