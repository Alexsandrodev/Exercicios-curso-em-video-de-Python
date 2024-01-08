#Variaveis
tabelaTimes = ('Botafogo', 'Bragantino', 'Grêmio', 'Palmeiras', 'Flamengo', 'Fluminense', 'Fluminense', 'Flamengo', 'Atlético-MG', 'Athletico-PR', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Cruzeiro', 'Corinthians', 'internacional', 'Santos', 'Goiás', 'Vasco da Gama', 'Bahia', 'América-MG', 'Coritiba')
cont = 0

#Mostra a tabela atual
print('Lista de times do brasileirão: ', end='')
for time in sorted(tabelaTimes):
    if cont < 21:
        print(time, end=', ')
    else:
        print(time, end='')

    cont += 1

print('')
print('-=-' * 37)
#Mostra os 5 primeiros times
cont = 0
print('Os 5 primeiros colocados são: ', end='')
for time in tabelaTimes[0:5]:
    if cont < 4:
        print(time, end=', ')
    else:
        print(time)
    cont += 1


print('-=-' * 37)
#Mostra os 4 últimos times
cont = 0
print('Os 4 últimos colocados são: ', end='')
for time in tabelaTimes[-1:-5: -1]:
    if cont <3:
        print(time, end=', ')

    else:
        print(time)

    cont += 1

print('-=-' * 37)
#mostra os times em ordem alfabetica
cont = 0
print('Os times em ordem alfabetica são: ', end='')
for time in sorted(tabelaTimes):
    if cont < 21:
        print(time, end=', ')
    else:
        print(time)

    cont += 1