termo1 = input('Primeiro Termo: ')
razao = input('Razão: ')
c = 1
mais = 10
total = 0
while type(termo1) == str and type(razao) == str:
    try:
        termo1 = float(termo1) 
        razao = float(razao)
    except ValueError:
        print('Por favor digite apenas números ') 
        termo1 = input('Primeiro Termo: ')
        razao = input('Razão: ')


while mais != 0:
    total += mais
    while c <= total:
        print(f'{termo1:.1f}', end=' ')
        termo1 += razao
        c += 1
    print('Pausa')
    mais = int(input('Quantos temos deseja mostrar a mais? '))
print('Fim')