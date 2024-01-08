# Funçoes
def area(a, b):
    area = a * b
    print(f'A área do seu terreno de {a:.1f}x{b:.1f} é {area}m².')

# Entrada de dados
print('\n Controle de terrenos')
print('-' * 25)

larg = float(input('Largura (m): '))
comp = float(input('Cumprimento (c): '))

# Saida de dados
area(larg, comp)