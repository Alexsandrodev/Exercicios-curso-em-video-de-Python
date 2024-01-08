r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro: '))

if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('Os segmentos a cima PODEM formar um triangulo' , end='')
    if r1 == r2 == r3:
        print('EQUILATERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓCELES')
else:
    print('Os segmentos a cima NÂO PODEM formar um triangulo')