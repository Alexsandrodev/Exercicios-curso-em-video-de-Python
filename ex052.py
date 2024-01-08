# numero = int(input('Digite um número: '))

# restos = []

# for c in range(2, numero):
#     restos.append(numero % c)
    
# if 0 in restos or numero == 1 or numero == 0:
#     print('\033[31m{} NÃO é um número primo\033[m'.format(numero))
# else:
#     print('\033[32m{} é um número primo\033[m'.format(numero))
    
numero = int(input('Digite um número: '))

tot = 0

for c in range(1, numero + 1 ):
    if numero % c == 0:
        print('\033[32m', end='')
        tot += 1
    else:
        print('\033[31m', end='')

    print('{}\033[m'.format(c), end=' ')

print(f'\nO número {numero} foi divisável {tot} vezes ')

if tot > 3:
    print(f'{numero} Não é primo')
else:
    print(f'{numero} é primo')