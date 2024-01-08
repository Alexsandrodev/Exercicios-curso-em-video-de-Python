produto = ''
preco = ''
valor_compras = 0
mais_de_1000 = 0
mais_barato = 0
produto_mais_barato = ''
cont = 0

while True: 
    cont += 1 
    produto = input(f'Nome do {cont}° produto: ').strip().capitalize()
    preco = input(f'Preço do {cont}° produto: ').strip()
    
    while type(preco) == str:
        try:
            preco = float(preco)
        except ValueError:
            preco = input('Preço do produto: ').strip()

    valor_compras += preco

    if preco >= 1000:
        mais_de_1000 += 1

    if cont == 1:
        mais_barato = preco
        produto_mais_barato = produto
    
    if cont > 1:
        if mais_barato > preco:
            mais_barato = preco
            produto_mais_barato = produto
    print('-=-' * 20)
    op = input('Para dastrar mais produtos digite [S], ou [N] para parar:').strip().lower()
    while op not in ('n', 's'):
        op = input('Para dastrar mais produtos digite [N], ou [N] para parar:').strip().lower()
    print('-=-' * 20)

    if op == 'n':
        break

print(f'preço da compra: R${valor_compras:.2f}')
print(f'{mais_de_1000} produtos foram mais de R$ 1000.00')
print(f'{produto_mais_barato} é o produto mais barato')