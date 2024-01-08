n = input('Digite um número inteiro: ')
a = 1
b = 1

while n.isdigit() == False:
    n = input('Por favor digite um número inteiro: ')

n = int(n)

i = 0

while i <= n:
    if i <= 1:
        print(i, end=' ')
        i += 1
    else:  
        a, b = b, a + b
        print (a, end=' ')
        i += 1

