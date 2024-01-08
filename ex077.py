palavras = ('nome', 'idade', 'programando', 'dormir', 'estudar', 'jogar', 'pular', 'rodadar')


for palavra in palavras:
    print(f'\nA palavra {palavra} tem como vogal: ', end='')
    for letras in range(0, len(palavra)):
        match palavra[letras]:
            case 'a':
                print('a', end=' ')
            case 'e':
                print('e', end=' ')
            case 'i':
                print('i', end=' ')
            case 'o':
                print('o', end=' ')
            case 'u':
                print('u', end=' ')
            case _:
                pass
