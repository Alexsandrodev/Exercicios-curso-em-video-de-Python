# Lista de valores e variaveis
valores = []

# loop de entrada de valores
while True:
    valor = int(input('Digite o valor: '))

    if valor in valores:
        print('Valor já existente')

    else:
        valores.append(valor)
        print('Valor adicionado com sucesso...')

    seguir = 'f'
    while seguir not in 'sn':
        seguir = input('Deseja continuar [S/N]. ').lower()[0]

    print('-=-' * 30)
    
    if seguir == 'n':
        break    

    else:
        pass


            
# Saida 
print(f'Os valor digitados em ordem cresente são: {sorted(valores)}')
