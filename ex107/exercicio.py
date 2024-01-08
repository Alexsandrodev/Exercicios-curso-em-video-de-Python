import moeda

preco = float(input('Digite um preço: R$'))

print(f'\nA metade de {preco} é {moeda.metade(preco)}')
print(f'o dobro de {preco} é {moeda.dobro(preco)}')
print(f'{preco} aumentado em 10% é igual á {moeda.aumentar(preco, 10)}')
print(f'{preco} descontando em 13% é igual á {moeda.diminuir(preco, 13)}')