# Importaçoes
from random import randint
from time import sleep

# Variaveis
cont = 1
num = 0
valores = []
cartelas = []
# Entrada de dados
print('-' * 50)
print(f'{"JOGAR NA MEGA CENA":^50}')
print('-' * 50)

jogos = int(input('\nQuantos jogos você deseja sortear? '))

print(f'\n{f"sorteando {jogos} jogos":-^50}')

# tratamento do dados
for jogo in range(0, jogos):
    for c in range(1, 7):
        num = randint(1, 60)
        
        while num in valores:
            num = randint(1, 60)
        else:
            valores.append(num)
    
    cartelas.append(sorted(valores)[:])
    valores.clear()

# Saida de dados

for cartela in cartelas:
    print(f'jogo {cont}: {cartela}')
    cont += 1
    sleep(1)

print(f'{"Tenha uma Boa Sorte":-^50}')