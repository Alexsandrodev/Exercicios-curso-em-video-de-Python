soma = 0
cont = 0
while True:
    num = input('Digite um número inteiro, ou [999] para para o programa: ')

    while type(num) == str:
        try:
            num = int(num)

        except ValueError:
            print('Valor invalido!')
            num = input('Por favor, digite um número inteiro: ')

    if num == 999:
        break

    cont += 1
    soma +=num

print(f'A soma dos {cont} números digitados é igual a {soma}')