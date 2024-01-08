produtos = ('Lapis', 1,
            'Caderno', 18,
            'Borracha', 3,
            'Bolacha', 2.5,
            'Café', 8,
            'moleton', 120)

print('-' * 40)
print(' '*10, 'Listagem de Produtos', ' ' * 10)
print('-' * 40)

for item in range(0, len(produtos), 2):

    letras = len(produtos[item])
    preco = float(produtos[item + 1])

    print(produtos[item], end='')
    print(f'{"." * (30 - letras)} R$ {preco:6,.2f}')