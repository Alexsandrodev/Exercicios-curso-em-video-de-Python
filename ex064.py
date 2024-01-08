n = 0
numeros = []

while n != 999:
    n = input('digite um número ou [999] para encerrar o programa:')

    while type(n) == str:
        try:
            n = float(n)
        except ValueError:
            n = input('Por favor, digite apenas números: ')
    
    if n != 999:
        numeros.append(n)


print(f' você digitou {len(numeros)} e a soma desses números é igual a {sum(numeros):.1f}')