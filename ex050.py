numeros = []

for c in range(0, 6):
    n = int(input('digite um número: '))
    if n % 2 == 0:
        numeros.append(n)
    

print(f' A soma dos {len(numeros)} números pares digitados  é {sum(numeros)}')