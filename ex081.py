# Variaveis e listas
valores = []
cont = 0

# Loop
while True:
# Entrada de dados
    num = int(input('valor a ser adicionado: '))
    print(f'Número {num} adicionado...')

# adiciona o número na variavel, e conta 1
    valores.append(num)
    cont += 1

# varifica o que foi digitado e se o usuário que ou não continuar
    while True:
        continuar = input('Deseja continuar? [S/N] ').strip().lower()[0]

        if continuar in 'sn':
            break

        else:
            pass

    
    print('-=-' * 30)
    
# Condição de parrada
    if continuar == 'n':
        break

# Saidas
print(f'Foram digitados {cont} números.')
print(f'Ordem dos valores digitados em ordem decresente: {sorted(valores, reverse=True)}')
if 5 in valores:
    print(f'O valor 5 foi digitado, e esta na {valores.index(5)}.')  
else:
    print('o valor 5 não foi digitado.')  