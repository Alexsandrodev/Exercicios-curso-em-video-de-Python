# Lista com os valores 
valores = []

# entrada de valores
for c in range(0, 5):
    valores.append(int(input(f'Digite o valor para a posição {c}: ')))

# Seleção dos valores
maior = max(valores)
menor = min(valores)

# Saida de valores
print('-' * 50)

print(f'Você digitou os valor: {valores}')

print(f'O maior valor digitado foi {maior} na posição ', end='')
# Laco para escrever as posições 
for c, valor in enumerate(valores):
    if valor == maior: 
        print(c, '', end='')
    else:
        pass


print(f'\nO menor valor digitado foi {min(valores)} na posição ', end='')
# Laco para escrever as posições 
for c, valor in enumerate(valores):
    if valor == menor: 
        print(c, '', end='')
    else:
        pass
