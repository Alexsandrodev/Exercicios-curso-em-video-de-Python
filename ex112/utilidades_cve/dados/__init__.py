def leiaDinheiro(msg):
    while True:
        v = input(f'{msg}').strip()
        if ',' in v:
            v = v.replace(',', '.')

        try:
            v = float(v)
            return v
        except ValueError:
            print(f'\033[31mErro! "{v}" é um preço invalido\033[m')