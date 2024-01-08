nome = str(input('digite seu nome completo: ')).strip()

print('analisando seu nome...')
print(f'Seu nome é em maiusculo é {nome.upper()}')
print(f'Seu nome é em minusculo é {nome.lower()}')
print('Seu nome é em maiusculo é {}'.format(len(nome) - nome.count(' ')))
print('Seu nome primeiro nome tem {} letras'.format(nome.find(' ')))
char = nome.find(' ')
print('Seu nome primeiro nome é {}'.format(nome[:char]))
