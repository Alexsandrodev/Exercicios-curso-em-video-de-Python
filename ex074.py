from random import randint

numeros = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))

print(f'Os valores sorteados foram : {numeros[0]}, {numeros[1]}, {numeros[2]}, {numeros[3]}, {numeros[4]}')
print(f' O maior valor é: {max(numeros)}')
print(f' O menor valor é: {min(numeros)}')