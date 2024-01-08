print('-=-' * 20)
print('Analisador de triângulos')
print('-=-' * 20)

a = float(input('Primeiro segmento '))
b = float(input('Segundo segmento '))
c = float(input('Terceiro segmento '))

if a + b > c and b + c > a and a + c > b:
    print('Os segmentos a cima PODEM formar um triangulo')
else:
    print('Os segmentos a cima NÂO PODEM formar um triangulo')