numeros = (int(input('Digite o 1° número: ')),
           int(input('Digite o 2° número: ')),
           int(input('Digite o 3° número: ')),
           int(input('Digite o 4° número: ')))
num_de_9 = 0
pos = 0

for num in numeros:
    if num == 9:
        num_de_9 +=1

for c in range(0, 4):
    if numeros[c] == 3:
        pos = c
        
print(f'Você digitou os valores: {numeros}')

print(f'O valor 9 apareceu {num_de_9} vezes')
if pos != False:
    print(f'O número 3 apareceu na {pos + 1}° posição')
else:
    print('O número 3 não apareceu em nenhuma posição')

print('Os valores pares digitados foram: ', end='')

for c in range(0,4):
    if numeros[c] % 2 == 0:
        print(numeros[c], end=' ')
    
