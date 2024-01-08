
op = 0
v1 = input('Digite o primeiro valor: ')
v2 = input('Digite o segundo valor: ')

while op != 5:

    if v1 and v2 not in '1 2 3 4 5 6 7 8 9 ':
        print('Por favor, digite apenas números ')
    else:
        n1 = float(v1)
        n2 = float(v2)

    
    print('O que deseja fazer com esses valore?')
    opcao = input("""[1] para somar
[2] para multiplicar
[3] para maior
[4] para novos numeros
[5] para sair do programa 
""")


    while opcao not in '1 2 3 4 5':
        print('por favor digite uma das opções a cima')
        
        opcao = input("""[1] para somar
[2] para multiplicar
[3] para maior
[4] para novos numeros
[5] para sair do programa 
""")
    
    op = int(opcao)

    if op == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
    elif op == 2:
        print(f'{n1} * {n2} = {n1 * n2}')
    elif op == 3:
        if n1 > n2:
            print(f'{n1} é o maior valor')
        else:
            print(f'{n2} é o maior valor')
    elif op == 4:
        print('Digite os novos valores ')
        v1 = input('Digite o primeiro valor: ')
        v2 = input('Digite o segundo valor: ')
    elif op == 5:
        print('Programa encerado!')
