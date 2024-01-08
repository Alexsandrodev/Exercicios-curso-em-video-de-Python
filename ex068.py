from random import randint

jogador = input('Par ou Impar? ').upper().strip()[0]
computador = ''
cont = 0

if jogador not in 'PI':
    jogador = input('Por favor, digite somente par ou impar')   


while True:
    numJogador = int(input('Qual valor de 0 a 10? '))
    numPc = randint(0, 10)
    print('')
    print(f'Você jogou {numJogador}')
    print(f'E o computador jogou {numPc}')
    while numJogador > 10:
        numJogador = input('Por favor, informe um valor de 0 a 10 somente: ')
    

    soma = numJogador + numPc

    if soma % 2 == 0 and jogador == 'P':
        print('Você ganhou')
        print('')
        cont += 1

    elif soma % 2 == 1 and jogador == 'I':
        print('Você ganhou ')
        print('')
        cont += 1

    else:
        print('O computador Ganhou')
        print('')
        break


print(f'Você ganhou {cont} vezes antes de perder')