n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))

media = (n1 + n2) / 2

if media < 5:
    print('\033[0;31mSua media foi {}, reprovado!\033[m'.format(media))
elif media < 7:
    print('\033[0;33mSua media foi {}, recuperação\033[m'.format(media))
else:
    print('\033[0;325mSua media foi {}, aprovado\033[m'.format(media))