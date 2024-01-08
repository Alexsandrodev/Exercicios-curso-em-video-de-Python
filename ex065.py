op = 's'
numeros = []
i = 1

while op != "n":
    numero = input(f'{i}° número intero: ') 
    i += 1 
    while type(numero) == str:
        try:
            numero = int(numero)
        except ValueError:
            numero = input('Por favor, digite apenas números inteiros: ')
    
    numeros.append(numero)
    op = input('Deseja continuar? [S/N] ').lower()
    while op not in 's, n':
        op = input(' Por favor, digite apenas "S" ou "N": ')

media = sum(numeros) / len(numeros)

print(f'Você digitou {len(numeros)}')
print(f'É a media desse números é igual a  {media:.1f}')
print(f'O menos valor digitado foi {min(numeros)} e o maior valor digitado foi {max(numeros)}')