idades = 0 
media_idade = 0
homem_mais_velho = ''
maior_idade_homen = 0
mulheres_menos_20 = 0

for c in range(1, 5):
    print('_____ {}° Pessoa _____'.format(c))
    nome = input('nome: ').title().strip()
    idade = int(input('idade: '))
    genero = input('Sexo [M/F]: ').upper().strip()
    
    idades += idade

    if c == 1 and genero == 'M':
        homem_mais_velho = nome
        maior_idade_homen = idade

    if idade > maior_idade_homen and genero == 'M':
        maior_idade_homen = idade
        homem_mais_velho = nome

    if genero == 'F' and idade < 21:
        mulheres_menos_20 += 1
    

media_idade = idades / c

print(f'A media de idade do grupo é {media_idade}')
print(f'O nome do homem mais velho tem {maior_idade_homen}, e se chama {homem_mais_velho}')
print(f'{mulheres_menos_20} mulheres tem menos de 20 anos')