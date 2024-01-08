farorial = input('Digite o numero no qual deseja fatorar: ')
soma = 0
cont = 0

while farorial.isdigit() == False:
    farorial = input('Por favor digite um número inteiro: ')

f = int(farorial)
cont = f
v = f * (f - 1)
f -= 1

if f <= 1:
    soma = 1

while f > 1:
    f -= 1
    v = v * f 
    if f == 1:
        soma = v



print(f'{farorial}! = ', end=(''))

while cont > 0 :
    if cont != 0:
        print(f'{cont} x', end=(' '))
    cont -= 1
else:
    print(f'{cont} = ', end=(''))

print(soma)