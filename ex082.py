# Listas e variaveis
valores = []
impares = []
pares = []

# Loop infinito para entrada de dados
while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    print(f'valor {num} adicionado na lista...')


# Laço para o usuário descidir se quer continuar ou não
    while True:
        continuar = input('Deseja continuar? [S/N] ').strip().lower()[0]

        if continuar in 'sn':
            break

    print('-=-' * 30)
# condição de parada do laço
    if continuar == 'n':
        break

for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

# Saida de dados
print('Os valores digitados foram: ', end='')
for valor in valores:
    print(f'{valor}, ', end='')

print('\nOs valor impares digitados foram: ',  end='')
for valor in impares:
    print(f'{valor}, ', end='')

print('\nOs valor pares digitados foram: ',  end='')
for valor in pares:
    print(f'{valor}, ',  end='')  