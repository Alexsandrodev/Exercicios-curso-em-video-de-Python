# Variaveis
matriz = [[], [], []] 
cont = 0 


# loop de entrada de dados
for x in range(0, 3):
    for y in range(0, 3):
        valor = int(input(f'Digite um valor para a [{x}, {y}]: '))
        matriz[x].append(valor)


# Saida de dados
print('-=-' * 30)
for lista in matriz:
    for num in lista:
        if cont != 3:
            print(f'[ {num:^3} ]', end=(''))
            cont += 1
        else:
            print(f'\n[ {num:^3} ]', end=(''))

            cont = 1
