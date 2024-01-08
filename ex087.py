# variaveis
matriz = [[], [], []] 
cont = 0
soma = 0
maior = 0

# loop para entrada de dados
for x in range(0, 3):
    for y in range(0,3):
        num = int(input(f'Digite o valor para a posição [{x}, {y}]: '))
        matriz[x].append(num)


# Tratamento e saida de dados
print('-=-' * 30)
for lista in matriz:
    for num in lista:
        if num % 2 == 0:
            soma += num

        if cont != 3:
            print(f'[ {num:^3} ]', end=(''))
            cont += 1
        else:
            print(f'\n[ {num:^3} ]', end=(''))

            cont = 1

maior = matriz[1][0]

if matriz[1][1] > maior:
    maior = matriz[1][1]
    
else:
    pass

if matriz[1][2] > maior:
    maior = matriz[1][2]

else:
    pass    

print()
print('-=-' * 30)

print(f'A soma de todos os valor digitados é {soma}')
print(f'A soma dos valores da terceira coluna é {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
print(f'O maior valor da segunda coluna é {maior}')