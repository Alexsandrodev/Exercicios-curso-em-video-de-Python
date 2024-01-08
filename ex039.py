import datetime

data = int(input('Informe o seu ano de nascimento: '))

atual =  datetime.date.today().year
idade = atual - data

if idade < 18:
    print('\033[0;31mVocê ainda não tem a idade correta para se alistar, volte com daqui a {} anos em {}\033[m'.format(18 - idade,  18 - idade + atual))
elif idade == 18:
    print('\033[0;32mVocê tem 18 anos, está na hora de se alistar\033[m')
else: 
    print('\033[0;33mvocê passou da idade de se alistar, O seu tempo foi a {} anos em {}\033[m'.format(idade - 18, atual - (idade - 18)))