valor = int(input('Escreva o número inteiro que deseja converter:  '))
modo = int(input('Digite [1] para Binário, [2] para octal, e [3] para hexadecimal: '))

if modo == 1:
    print('{} convertido para binário é {}'.format(valor, bin(valor)[2:]))
elif modo == 2:
    print('{} convertido para octal é {}'.format(valor, oct(valor)[2:]))
elif modo == 3:
    print('{} convertido para hexadecimal é {}'.format(valor, hex(valor)[2:]))
else:
    print('\033[31mVALOR INVALIDO\033[m')