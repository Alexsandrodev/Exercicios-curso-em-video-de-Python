n = int(input('digite um número: '))

print('A tabuada do número {} é'.format(n))

for i in range(0, 11):
    valor = i * n
    print('{:2} X {:2} = {:2}'.format(i, n, valor))