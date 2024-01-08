n =  int(input('Digite um número: '))

resto = n % 2

if resto == 0:
    print(f'O número {n} é par')
else:
    print(f'O número {n} é impar')