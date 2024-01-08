sx = input('Digite seu sexo: [F/M] ').strip().upper()

while sx not in 'F M':
    print('Erro, por favor digite novamente.')
    print('O valor tem que ser [F] ou [M].')
    sx = input('Digite seu sexo: [F/M] ')

if sx == 'F':
    print('Você é uma mulher')
else:
    print('Você é um homem')
