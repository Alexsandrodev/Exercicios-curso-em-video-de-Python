import moeda

preco = float(input('Digite um preço: R$ '))

print(f'\nA metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
print(f'o dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}')
print(f'{moeda.moeda(preco)} aumentado em 10% é igual á {moeda.aumentar(preco, 10, True)}')
print(f'{moeda.moeda(preco)} descontando em 13% é igual á {moeda.diminuir(preco, 13, True)}')