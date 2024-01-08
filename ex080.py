# Listas e variaveis
valores = []
num = 0
a = 0
b = 0

# entradas do usuário
for c in range(1,6):
    num = int(input(f'Digite o {c}° valor: '))
    
    valores.append(num)

# loop para a organização dos itens na lista
for c in range(0, 6):
    if valores[3] > valores[4]:
        a = valores[3]
        b = valores[4]
        valores[4] = a
        valores[3] = b


    if valores[2] > valores[3]:
        a = valores[2]
        b = valores[3]
        valores[3] = a
        valores[2] = b    

    if valores[1] > valores[2]:
        a = valores[1]
        b = valores[2]
        valores[2] = a
        valores[1] = b   

    if valores[0] > valores[1]:
        a = valores[0]
        b = valores[1]
        valores[1] = a
        valores[0] = b     

# Saidas e
print(f'Esses são os valores digitados em ordem númerica {valores}')