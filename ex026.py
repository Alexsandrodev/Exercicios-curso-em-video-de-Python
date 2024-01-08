f = str(input('digite uma frase: ')).lower().strip()

print('A letra A apareceu {} veses na frase'.format(f.count('a')))
print('A primeira letra A apareceu na posição {}'.format(f.find('a') + 1))
print('A última letra A apareceu na posição {}'.format(f.rfind('a') + 1))