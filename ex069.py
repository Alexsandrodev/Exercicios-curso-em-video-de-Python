nome = ''
idade = 0
sexo = ''
i = 0
mais_de_18 = 0
qts_homens = 0
mulheres_menos_20 = 0


while True:
    i += 1
    print('-=-' * 30)
    print(f'       {i}° pessoa')
    print('-=-' * 30)
    nome = input(f'nome da pessoa: ').strip()
    idade = input('Qual a idade dessa pessoa: ')

    while type(idade) == str:
        try:
            idade = int(idade)

        except ValueError:
            idade = input('Qual a idade dessa pessoa: ')      
                 
    sexo = input('Sexo da pessoa [M/F]: ').strip().lower()

    while sexo not in 'fm':
        sexo = input('Sexo da pessoa [M/F]: ').strip().lower()       

    if idade > 18:
        mais_de_18 += 1
    
    if sexo == 'm':
        qts_homens += 1
    
    if idade < 20 and sexo == 'f':
        mulheres_menos_20 += 1

    print('-=-' * 30)
    op = input('Digite [S] para continurar, ou [N] para parar o programa: ').strip().lower()

    if op == 'n':
        break

print('-=-' * 30)
print(f'{mais_de_18} pessoas tem mais de 18 anos')
print(f'{qts_homens} homens foram cadastados')
print(f'{mulheres_menos_20} mulheres com menos de 20 anos foram cadastradas')
