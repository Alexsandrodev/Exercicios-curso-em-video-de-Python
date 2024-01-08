from random import randint

print('________Jogo de Adivinhação________')
computador = randint(0, 10)
usuario = input('Digite um número de  0 a 10: ')
cont = 0


while str(computador) != usuario:
    if usuario.isdigit() == False:
        usuario = input('\033[31mPor favor digite um numero:\033[m ')
    else:
        cont += 1
        usuario = int(usuario)
        computador = int(computador)
        print('\033[31mVocê errou\033[m')
        if usuario > computador:
            print('Menos...', end=' ')
        else:
            print('Mais...', end=' ')
        usuario = input('Tente novamente : ')

print('\033[32mPARABENS\033[m')
print(f'Depois de {cont} tentativas você acertou ')