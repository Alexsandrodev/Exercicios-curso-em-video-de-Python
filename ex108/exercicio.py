import moeda

preco = float(input('Digite um preço: R$ '))

print(f'\nA metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
print(f'o dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')
print(f'{moeda.moeda(preco)} aumentado em 10% é igual á {moeda.moeda(moeda.aumentar(preco, 10))}')
print(f'{moeda.moeda(preco)} descontando em 13% é igual á {moeda.moeda(moeda.diminuir(preco, 13))}')