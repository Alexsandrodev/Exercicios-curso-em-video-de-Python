termo1 = int(input('primeiro termo: '))
razão = int(input('razão: '))

decimo = termo1 + (10 - 1) * razão

for c in range(termo1, decimo + razão ,razão):
    print(f'{c}', end=' ')