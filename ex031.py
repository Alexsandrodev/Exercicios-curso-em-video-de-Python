km = float(input('Qual é a distância da sua viagem? '))

print(f'Você está em uma viagem de {km}km.') 

if km < 200:
    print('O preço da sua passagem será de R${:.2f}'.format(km * 0.5))
else:
    print('O preço da sua passagem será de R${:.2f}'.format(km * 0.45))