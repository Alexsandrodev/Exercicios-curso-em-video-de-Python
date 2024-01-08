# Variaveis
valores = [[], []] 
cont1 = 0
cont2 = 0

# Laço para entrada de dados

for c in range(1, 8):
    num = int(input(f'Digite o {c}° valor: '))
    
    if num % 2 == 0:
        if cont1 == 0:
            valores[0].append(num)
        elif valores[0][-1] <= num:
            valores[0].append(num)
        elif valores[0][0] > num:
            valores[0].insert(0, num) 

        cont1 += 1   
    else:
        if cont2 == 0:
            valores[1].append(num)
        elif valores[1][-1] <= num:
            valores[1].append(num)
        elif valores[1][0] > num:
            valores[1].insert(0, num)    

        cont2 += 1

print('-=-' * 30)
    
print(f'Os valores pares digitados foram: {valores[0]}')
print(f'Os valores impares digitados foram: {valores[1]}')