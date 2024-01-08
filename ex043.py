peso = float(input('informe o seu peso: (km) '))
altura = float(input('infome a sua altura: (m) '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('imc de: {:.1f} \033[0;31mAbaixo do peso\033[m'.format(imc))
elif imc < 25:
    print('imc de: {:.1f} \033[0;32mPeso ideal\033[m'.format(imc))
elif imc < 30:
    print('imc de: {:.1f} \033[0;31mSobrepeso\033[m'.format(imc))
elif imc < 40:
    print('imc de: {:.1f} \033[0;31mSobrepeso\033[m'.format(imc))
else:
    print('imc de: {:.1f} \033[0;31mObesidade mórbida\033[m'.format(imc))
