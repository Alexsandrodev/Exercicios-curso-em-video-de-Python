while True:
    print('_' * 96)
    n = int(input('Digite o número que deseja multiplicar, caso o valor seja negativo o programa se encerra: '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} X {c} = {n * c}')

print('Programa encerrado')