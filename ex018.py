from math import sin, tan, cos, radians

ang = float(input('digite o angulo que você deseja: '))

sen = sin(radians(ang))
con = cos(radians(ang))
tag = tan(radians(ang))

print(f'O angulo de {ang} tem o SENO de {sen:.2f}')
print(f'O angulo de {ang} tem o COSSENO de {con:.2f}')
print(f'O angulo de {ang} tem o TANGENTE de {tag:.2f}')