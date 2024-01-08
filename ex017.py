from math import hypot

co = float(input('comprimento do cateto oposto: '))
ca = float(input('compromento do cateto adjacente: '))

hi = hypot(co, ca)

print(f'A hiporenusa vai medir {hi:.2f}')