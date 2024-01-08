termo1 = input('Primeiro Termo: ')
razao = input('Razão: ')
c = 1
while type(termo1) == str and type(razao) == str:
    try:
        termo1 = float(termo1) 
        razao = float(razao)
    except ValueError:
        print('Por favor digite apenas números ') 
        termo1 = input('Primeiro Termo: ')
        razao = input('Razão: ')



while c <= 10:
    print(f'{termo1:.1f}', end=' ')
    termo1 += razao
    c += 1